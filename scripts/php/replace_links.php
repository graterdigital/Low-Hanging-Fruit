<?php
/**
 * Rewrite internal links that point at redirecting URLs so they point at the final URL.
 * Runs inside WordPress via `wp eval-file`. Reads a JSON job from the REPLACE_LINKS_JOB constant
 * that the Python runner prepends. Never call this file directly.
 *
 * Job: {"mode": "dry"|"apply", "host": "hsfamilylaw.com", "swaps": [{"old": "...", "new": "..."}]}
 *
 * Matching is anchored so a URL is only replaced when it is a complete link target:
 *   preceded by a quote or "(" and followed by a quote, ")", "#" or "?".
 * That is what keeps /child-support/ from matching inside /divorce/child-support/,
 * and /contact-us from matching /contact-us/.
 * Both absolute (https://host/path) and root-relative (/path) forms are handled; a relative
 * link stays relative after the swap.
 *
 * Scope: post_content of every non-revision post, and postmeta values (menus, ACF links).
 * Applies with wp_update_post so WordPress keeps a revision of the previous content.
 */
if (!defined('REPLACE_LINKS_JOB')) { fwrite(STDERR, "no job\n"); exit(1); }
$job   = json_decode(REPLACE_LINKS_JOB, true);
$mode  = $job['mode'] ?? 'dry';
$host  = preg_quote($job['host'], '~');
global $wpdb;

$rules = [];
foreach ($job['swaps'] as $s) {
    $oldPath = preg_replace('~^https?://(www\.)?[^/]+~', '', $s['old']);
    $newPath = preg_replace('~^https?://(www\.)?[^/]+~', '', $s['new']);
    $q = preg_quote($oldPath, '~');
    // absolute form
    $rules[] = ['re' => '~(?<=["\'(])https?://(?:www\.)?' . $host . $q . '(?=["\')#?])~', 'to' => $s['new'], 'old' => $s['old']];
    // root-relative form
    $rules[] = ['re' => '~(?<=["\'(])' . $q . '(?=["\')#?])~', 'to' => $newPath, 'old' => $s['old']];
    // JSON-escaped forms, as stored in block-editor comments and ACF block data: https:\/\/host\/path\/ inside \"...\"
    $qj = preg_quote(str_replace('/', '\\/', $oldPath), '~');
    $newJ = str_replace('/', '\\/', $s['new']); $newPathJ = str_replace('/', '\\/', $newPath);
    $rules[] = ['re' => '~(?<=\\")https?:\\\\/\\\\/(?:www\\.)?' . $host . $qj . '(?=\\\\?["#?])~', 'to' => $newJ, 'old' => $s['old']];
    $rules[] = ['re' => '~(?<=\\")' . $qj . '(?=\\\\?["#?])~', 'to' => $newPathJ, 'old' => $s['old']];
}

// Probe mode: report every raw occurrence of each old path anywhere in posts, postmeta and options,
// with context, so unmatched links can be located. Changes nothing.
if ($mode === 'probe') {
    $rep = [];
    foreach ($job['swaps'] as $s) {
        $path = preg_replace('~^https?://(www\.)?[^/]+~', '', $s['old']);
        $needles = [$path, str_replace('/', '\\/', $path)];
        foreach ($needles as $n) {
            $like = '%' . $wpdb->esc_like($n) . '%';
            foreach ($wpdb->get_results($wpdb->prepare("SELECT ID, post_type, post_status, post_title, post_content FROM {$wpdb->posts} WHERE post_type<>'revision' AND post_content LIKE %s", $like)) as $r) {
                foreach (ctx($r->post_content, $n) as $c) $rep[] = ['old' => $s['old'], 'where' => "post {$r->ID} ({$r->post_type}/{$r->post_status}) {$r->post_title}", 'ctx' => $c];
            }
            foreach ($wpdb->get_results($wpdb->prepare("SELECT meta_id, post_id, meta_key, meta_value FROM {$wpdb->postmeta} WHERE meta_value LIKE %s", $like)) as $r) {
                foreach (ctx($r->meta_value, $n) as $c) $rep[] = ['old' => $s['old'], 'where' => "postmeta {$r->meta_id} post {$r->post_id} key {$r->meta_key}", 'ctx' => $c];
            }
            foreach ($wpdb->get_results($wpdb->prepare("SELECT option_name, option_value FROM {$wpdb->options} WHERE option_value LIKE %s", $like)) as $r) {
                foreach (ctx($r->option_value, $n) as $c) $rep[] = ['old' => $s['old'], 'where' => "option {$r->option_name}", 'ctx' => $c];
            }
        }
    }
    echo "\n===JSON===\n" . json_encode(['mode' => 'probe', 'occurrences' => $rep], JSON_UNESCAPED_SLASHES) . "\n";
    exit(0);
}
function ctx($hay, $needle) {
    $out = []; $off = 0;
    while (($i = strpos($hay, $needle, $off)) !== false) {
        $out[] = substr($hay, max(0, $i - 70), strlen($needle) + 140); $off = $i + strlen($needle);
        if (count($out) > 5) break;
    }
    return $out;
}

function apply_rules($text, $rules, &$hits) {
    foreach ($rules as $r) {
        $n = 0;
        $text = preg_replace($r['re'], $r['to'], $text, -1, $n);
        if ($n) { $hits[$r['old']] = ($hits[$r['old']] ?? 0) + $n; }
    }
    return $text;
}

$out = ['mode' => $mode, 'posts' => [], 'meta' => [], 'totals' => []];

// Posts
$ids = $wpdb->get_col("SELECT ID FROM {$wpdb->posts} WHERE post_type NOT IN ('revision','nav_menu_item') AND post_status NOT IN ('trash','auto-draft')");
foreach ($ids as $id) {
    $p = get_post($id);
    if (!$p || $p->post_content === '') continue;
    $hits = [];
    $new = apply_rules($p->post_content, $rules, $hits);
    if ($new === $p->post_content) continue;
    $entry = ['id' => (int)$id, 'type' => $p->post_type, 'status' => $p->post_status, 'title' => $p->post_title,
              'url' => get_permalink($id), 'hits' => $hits, 'before' => $p->post_content, 'after' => $new];
    if ($mode === 'apply') {
        $r = wp_update_post(wp_slash(['ID' => $id, 'post_content' => $new]), true);
        $entry['applied'] = is_wp_error($r) ? 'ERROR: ' . $r->get_error_message() : true;
    }
    $out['posts'][] = $entry;
    foreach ($hits as $k => $v) $out['totals'][$k] = ($out['totals'][$k] ?? 0) + $v;
}

// Postmeta (menu item URLs, ACF link fields). Serialized values are left alone and reported.
$like = '%' . $wpdb->esc_like($job['host']) . '%';
$rows = $wpdb->get_results($wpdb->prepare("SELECT meta_id, post_id, meta_key, meta_value FROM {$wpdb->postmeta} WHERE meta_key NOT LIKE '\_edit%%' AND (meta_value LIKE %s OR meta_value LIKE '/%%')", $like));
foreach ($rows as $m) {
    if (is_serialized($m->meta_value)) {
        $hits = [];
        apply_rules($m->meta_value, $rules, $hits);
        if ($hits) $out['meta'][] = ['meta_id' => (int)$m->meta_id, 'post_id' => (int)$m->post_id, 'key' => $m->meta_key, 'hits' => $hits, 'skipped' => 'serialized value; fix by hand'];
        continue;
    }
    $hits = [];
    $new = apply_rules($m->meta_value, $rules, $hits);
    // Plain exact-URL values (e.g. _menu_item_url) have no quotes to anchor on; handle them as a whole-value match.
    if ($new === $m->meta_value) {
        foreach ($job['swaps'] as $s) {
            if (rtrim($m->meta_value, '/') === rtrim($s['old'], '/') && $m->meta_value === $s['old']) { $new = $s['new']; $hits[$s['old']] = 1; }
        }
    }
    if ($new === $m->meta_value) continue;
    $entry = ['meta_id' => (int)$m->meta_id, 'post_id' => (int)$m->post_id, 'key' => $m->meta_key, 'hits' => $hits, 'before' => $m->meta_value, 'after' => $new];
    if ($mode === 'apply') {
        $entry['applied'] = (bool)$wpdb->update($wpdb->postmeta, ['meta_value' => $new], ['meta_id' => $m->meta_id]);
    }
    $out['meta'][] = $entry;
    foreach ($hits as $k => $v) $out['totals'][$k] = ($out['totals'][$k] ?? 0) + $v;
}

echo "\n===JSON===\n" . json_encode($out, JSON_UNESCAPED_SLASHES) . "\n";
