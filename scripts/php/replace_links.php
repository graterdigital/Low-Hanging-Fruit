<?php
/**
 * Rewrite internal links that point at redirecting URLs so they point at the final URL.
 * Runs inside WordPress via `wp eval-file`; the Python runner prepends the job as REPLACE_LINKS_JOB.
 *
 * Job: {"mode": "dry"|"apply"|"probe", "host": "example.com", "legacy_hosts": ["old.wpengine.com"],
 *       "swaps": [{"old": "https://example.com/old/", "new": "https://example.com/new/"}]}
 *
 * Hosts: links are matched on the live domain, on whatever host this install currently runs on
 * (staging copies get their own domain), and on any legacy hosts. A matched link keeps the host it
 * had, except legacy hosts, which become the current host. Only the path changes otherwise.
 *
 * Anchoring: a URL is replaced only when it is a complete link target (between quotes/parens, or a whole
 * string value inside serialized/JSON data). /child-support/ never matches inside /divorce/child-support/.
 * Forms handled: absolute, root-relative, JSON-escaped (https:\/\/...), and PHP-serialized values
 * (ACF link/url fields), which are unserialized, rewritten, and reserialized.
 *
 * Scope: post_content of non-revision posts, and postmeta values. wp_update_post keeps a revision.
 * wp_options is scanned and reported (the `options` key in the output) but never written.
 */
if (!defined('REPLACE_LINKS_JOB')) { fwrite(STDERR, "no job\n"); exit(1); }
// wp eval-file includes this file inside a function, so declare shared state global explicitly
// or the helper functions below see nothing.
global $wpdb, $job, $mode, $home_host, $live_host, $legacy, $all_hosts, $hosts_re, $swaps;
$job  = json_decode(REPLACE_LINKS_JOB, true);
$mode = $job['mode'] ?? 'dry';

$home_host   = parse_url(home_url(), PHP_URL_HOST);
$live_host   = $job['host'];
$legacy      = array_values(array_filter($job['legacy_hosts'] ?? []));
$all_hosts   = array_values(array_unique(array_merge([$live_host, $home_host], $legacy)));   // array_values: a gapped array would JSON-encode as an object
$hosts_re    = '(?:www\.)?(?:' . implode('|', array_map(fn($h) => preg_quote(preg_replace('~^www\.~', '', $h), '~'), $all_hosts)) . ')';
$path_of     = fn($u) => preg_replace('~^https?://(www\.)?[^/]+~', '', $u);

$swaps = []; $refused = [];
foreach ($job['swaps'] as $s) {
    $op = $path_of($s['old']); $np = $path_of($s['new']);
    // A path with a backslash, quote, space or angle bracket cannot be anchored safely: "/x/\\" matches the escaping
    // backslash of a JSON-encoded link and the rewrite eats it. Refuse such swaps outright, whatever the map says.
    if (preg_match('~[\\\\"\'<>\s]~', $op . $np) || $op === '' || $op === '/') { $refused[] = ['old' => $s['old'], 'reason' => 'unsafe characters in path']; continue; }
    $swaps[] = ['old' => $s['old'], 'oldPath' => $op, 'newPath' => $np];
}
/** Valid JSON and not a bare scalar: the shape builder data (Elementor) takes. */
function is_json_blob($v) { if (!is_string($v) || $v === '' || ($v[0] !== '{' && $v[0] !== '[')) return false; json_decode($v); return json_last_error() === JSON_ERROR_NONE; }

function target_host($matched_host) {
    global $legacy, $home_host;
    $bare = preg_replace('~^www\.~', '', $matched_host);
    foreach ($legacy as $l) if ($bare === preg_replace('~^www\.~', '', $l)) return $home_host;
    return $matched_host;
}

/** Rewrite one string. $hits accumulates counts per old URL. */
function rewrite($text, &$hits) {
    global $swaps, $hosts_re, $legacy, $home_host;
    foreach ($swaps as $s) {
        $q  = preg_quote($s['oldPath'], '~');
        $qj = preg_quote(str_replace('/', '\\/', $s['oldPath']), '~');
        $newJ = str_replace('/', '\\/', $s['newPath']);
        $n = 0;
        // absolute: "https://host/old/"  → same host (or home host for legacy), new path
        $text = preg_replace_callback('~(?<=["\'(])(https?://)(' . $hosts_re . ')' . $q . '(?=["\')#?])~i',
            fn($m) => $m[1] . target_host($m[2]) . $s['newPath'], $text, -1, $c); $n += $c;
        // root-relative: "/old/"
        $text = preg_replace('~(?<=["\'(])' . $q . '(?=["\')#?])~', $s['newPath'], $text, -1, $c); $n += $c;
        // JSON-escaped absolute and relative
        $text = preg_replace_callback('~(?<=\\\\")(https?:\\\\/\\\\/)(' . $hosts_re . ')' . $qj . '(?=\\\\?["#?])~i',
            fn($m) => $m[1] . target_host($m[2]) . $newJ, $text, -1, $c); $n += $c;
        $text = preg_replace('~(?<=\\\\")' . $qj . '(?=\\\\?["#?])~', $newJ, $text, -1, $c); $n += $c;
        if ($n) $hits[$s['old']] = ($hits[$s['old']] ?? 0) + $n;
    }
    // Legacy host on an otherwise-correct path: just move it to the current host.
    foreach ($legacy as $l) {
        $lq = preg_quote(preg_replace('~^www\.~', '', $l), '~');
        $text = preg_replace('~(?<=["\'(])(https?://)(?:www\.)?' . $lq . '(?=/)~i', '$1' . $home_host, $text, -1, $c);
        if ($c) $hits["host:$l"] = ($hits["host:$l"] ?? 0) + $c;
    }
    return $text;
}

/** Rewrite a scalar that is a whole URL value (serialized/array leaf), not embedded in markup. */
function rewrite_value($v, &$hits) {
    global $swaps, $hosts_re, $legacy, $home_host;
    if (!is_string($v)) return $v;
    if (preg_match('~^(https?://)(' . $hosts_re . ')(/.*)$~i', $v, $m) || preg_match('~^()()(/[^\s"\']*)$~', $v, $m)) {
        [$all, $scheme, $host, $path] = $m;
        foreach ($swaps as $s) {
            if ($path === $s['oldPath']) { $hits[$s['old']] = ($hits[$s['old']] ?? 0) + 1; return $scheme . ($host ? target_host($host) : '') . $s['newPath']; }
        }
        if ($host && target_host($host) !== $host) { $hits["host:$host"] = ($hits["host:$host"] ?? 0) + 1; return $scheme . target_host($host) . $path; }
        return $v;
    }
    return rewrite($v, $hits);   // HTML inside a WYSIWYG field
}
function walk($data, &$hits) {
    if (is_array($data)) { foreach ($data as $k => $v) $data[$k] = walk($v, $hits); return $data; }
    return rewrite_value($data, $hits);
}

/** Anchored find-regex for an old path (plain or JSON-escaped form). Matches the path as a root-relative link or
 *  directly after a scheme://host, never inside a longer path (/x/ in /y/x/) and never followed by more path. */
function find_re($needle) {
    $host = '(?:https?:\\\\?/\\\\?/[^/"\'\s\\\\]+)?';
    return '~(?<![\w/\\\\-])' . $host . preg_quote($needle, '~') . '(?![\w/\\\\-])~i';
}

/** Anchored scan of wp_options for old paths and legacy hosts. Report only; options are never edited.
 *  Every mode calls this so the Python runner can write the companion -options.md log. */
function scan_options() {
    global $wpdb, $swaps, $legacy;
    $rep = []; $seen = [];
    $needles = [];
    // find_re() rejects a trailing `/` or `\`, so an old path without a trailing slash (/contact-us) does not match
    // its own slashed successor (/contact-us/). Transients are skipped: they are caches, not settings.
    foreach ($swaps as $s) foreach ([$s['oldPath'], str_replace('/', '\\/', $s['oldPath'])] as $n) $needles[] = [$s['old'], $n, find_re($n)];
    foreach ($legacy as $l) $needles[] = ["host:$l", $l, '~' . preg_quote($l, '~') . '~i'];
    foreach ($needles as [$old, $needle, $re]) {
        $like = '%' . $wpdb->esc_like($needle) . '%';
        foreach ($wpdb->get_results($wpdb->prepare("SELECT option_name, option_value, autoload FROM {$wpdb->options} WHERE option_value LIKE %s AND option_name NOT LIKE '\\_transient\\_%%' AND option_name NOT LIKE '\\_site\\_transient\\_%%'", $like)) as $r) {
            if (isset($seen[$r->option_name . "\0" . $old])) continue;
            if (!preg_match($re, $r->option_value, $m, PREG_OFFSET_CAPTURE)) continue;
            $seen[$r->option_name . "\0" . $old] = 1;
            $rep[] = ['option_name' => $r->option_name, 'autoload' => $r->autoload, 'size' => strlen($r->option_value), 'old' => $old,
                      'ctx' => substr($r->option_value, max(0, $m[0][1] - 60), strlen($m[0][0]) + 120)];
        }
    }
    return $rep;
}

// ---- checkjson: is every _elementor_data row still valid JSON? (damage check after a bad run) ----
if ($mode === 'checkjson') {
    $bad = []; $n = 0;
    foreach ($wpdb->get_results("SELECT m.meta_id, m.post_id, p.post_type, p.post_status, p.post_title FROM {$wpdb->postmeta} m JOIN {$wpdb->posts} p ON p.ID = m.post_id WHERE m.meta_key = '_elementor_data' AND p.post_type <> 'revision'") as $r) {
        $n++; $v = get_post_meta($r->post_id, '_elementor_data', true);
        if (!is_string($v) || $v === '' || $v === '[]') continue;
        json_decode($v);
        if (json_last_error() !== JSON_ERROR_NONE) $bad[] = ['meta_id' => (int)$r->meta_id, 'post_id' => (int)$r->post_id, 'type' => $r->post_type, 'status' => $r->post_status, 'title' => $r->post_title, 'error' => json_last_error_msg(), 'url' => get_permalink($r->post_id)];
    }
    echo "\n===JSON===\n" . json_encode(['mode' => 'checkjson', 'home_host' => $home_host, 'hosts' => $all_hosts, 'checked' => $n, 'invalid' => $bad], JSON_UNESCAPED_SLASHES) . "\n";
    exit(0);
}

// ---- probe: where do the old paths live? (anchored so /x/ doesn't match /y/x/) ----
if ($mode === 'probe') {
    $rep = [];
    foreach ($swaps as $s) {
        foreach ([$s['oldPath'], str_replace('/', '\\/', $s['oldPath'])] as $needle) {
            $like = '%' . $wpdb->esc_like($needle) . '%';
            $re = find_re($needle);
            $scan = function($text, $where) use (&$rep, $re, $s) {
                if (!preg_match_all($re, $text, $mm, PREG_OFFSET_CAPTURE)) return;
                foreach (array_slice($mm[0], 0, 5) as $m) $rep[] = ['old' => $s['old'], 'where' => $where, 'ctx' => substr($text, max(0, $m[1] - 70), strlen($m[0]) + 140)];
            };
            foreach ($wpdb->get_results($wpdb->prepare("SELECT ID, post_type, post_status, post_title, post_content FROM {$wpdb->posts} WHERE post_type NOT IN ('revision','customize_changeset') AND post_content LIKE %s", $like)) as $r)
                $scan($r->post_content, "post {$r->ID} ({$r->post_type}/{$r->post_status}) {$r->post_title}");
            foreach ($wpdb->get_results($wpdb->prepare("SELECT meta_id, post_id, meta_key, meta_value FROM {$wpdb->postmeta} WHERE meta_value LIKE %s", $like)) as $r)
                $scan($r->meta_value, "postmeta {$r->meta_id} post {$r->post_id} key {$r->meta_key}");
            foreach ($wpdb->get_results($wpdb->prepare("SELECT option_name, option_value FROM {$wpdb->options} WHERE option_value LIKE %s", $like)) as $r)
                $scan($r->option_value, "option {$r->option_name}");
        }
    }
    foreach ($legacy as $l) {
        $like = '%' . $wpdb->esc_like($l) . '%';
        $n1 = (int)$wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_type<>'revision' AND post_content LIKE %s", $like));
        $n2 = (int)$wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM {$wpdb->postmeta} WHERE meta_value LIKE %s", $like));
        $rep[] = ['old' => "host:$l", 'where' => "$n1 posts, $n2 meta rows reference this legacy host", 'ctx' => ''];
    }
    echo "\n===JSON===\n" . json_encode(['mode' => 'probe', 'home_host' => $home_host, 'hosts' => $all_hosts, 'occurrences' => $rep], JSON_UNESCAPED_SLASHES) . "\n";
    exit(0);
}

$out = ['mode' => $mode, 'home_host' => $home_host, 'hosts' => $all_hosts, 'posts' => [], 'meta' => [], 'totals' => [], 'options' => scan_options(), 'refused' => $refused, 'json_guarded' => []];
$tally = function($hits) use (&$out) { foreach ($hits as $k => $v) $out['totals'][$k] = ($out['totals'][$k] ?? 0) + $v; };

// ---- postmeta first: any value containing an old path (plain or JSON-escaped) or a legacy host, on non-revision posts.
// (Meta goes before posts because wp_update_post creates revisions whose copied meta would otherwise be found and counted.)
$conds = []; $params = [];
foreach ($swaps as $s) foreach ([$s['oldPath'], str_replace('/', '\\/', $s['oldPath'])] as $n) { $conds[] = "m.meta_value LIKE %s"; $params[] = '%' . $wpdb->esc_like($n) . '%'; }
foreach ($legacy as $l) { $conds[] = "m.meta_value LIKE %s"; $params[] = '%' . $wpdb->esc_like($l) . '%'; }
$rows = $conds ? $wpdb->get_results($wpdb->prepare("SELECT m.meta_id, m.post_id, m.meta_key, m.meta_value FROM {$wpdb->postmeta} m JOIN {$wpdb->posts} p ON p.ID = m.post_id WHERE p.post_type NOT IN ('revision','customize_changeset') AND m.meta_key NOT LIKE '\\_edit%%' AND (" . implode(' OR ', $conds) . ")", $params)) : [];
foreach ($rows as $m) {
    $hits = [];
    if (is_serialized($m->meta_value)) {
        $data = maybe_unserialize($m->meta_value);
        $newData = walk($data, $hits);
        $new = $hits ? serialize($newData) : $m->meta_value;
        $kind = 'serialized';
    } else {
        $new = rewrite_value($m->meta_value, $hits); $kind = is_json_blob($m->meta_value) ? 'json' : 'plain';
    }
    if ($new === $m->meta_value) continue;
    $e = ['meta_id' => (int)$m->meta_id, 'post_id' => (int)$m->post_id, 'key' => $m->meta_key, 'kind' => $kind, 'hits' => $hits, 'before' => $m->meta_value, 'after' => $new];
    // JSON guard: never turn a valid JSON blob into an invalid one, whatever the swap rules say.
    if ($kind === 'json' && !is_json_blob($new)) { $e['applied'] = 'GUARDED: rewrite would break JSON'; unset($e['after']); $out['json_guarded'][] = $e; continue; }
    if ($mode === 'apply') $e['applied'] = (bool)$wpdb->update($wpdb->postmeta, ['meta_value' => $new], ['meta_id' => $m->meta_id]);
    $out['meta'][] = $e; $tally($hits);
}

// ---- posts ----
$ids = $wpdb->get_col("SELECT ID FROM {$wpdb->posts} WHERE post_type NOT IN ('revision','nav_menu_item','customize_changeset') AND post_status NOT IN ('trash','auto-draft')");
foreach ($ids as $id) {
    $p = get_post($id);
    if (!$p || $p->post_content === '') continue;
    $hits = []; $new = rewrite($p->post_content, $hits);
    if ($new === $p->post_content) continue;
    $e = ['id' => (int)$id, 'type' => $p->post_type, 'status' => $p->post_status, 'title' => $p->post_title, 'url' => get_permalink($id), 'hits' => $hits, 'before' => $p->post_content, 'after' => $new];
    if ($mode === 'apply') { $r = wp_update_post(wp_slash(['ID' => $id, 'post_content' => $new]), true); $e['applied'] = is_wp_error($r) ? 'ERROR: ' . $r->get_error_message() : true; }
    $out['posts'][] = $e; $tally($hits);
}

echo "\n===JSON===\n" . json_encode($out, JSON_UNESCAPED_SLASHES) . "\n";
