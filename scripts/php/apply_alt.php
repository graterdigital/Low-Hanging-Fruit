<?php
/**
 * Write alt text from a reviewed CSV. Runs inside WordPress via `wp eval-file`; the runner prepends APPLY_ALT_JOB.
 *
 * Job: {"mode": "dry"|"apply", "rows": [
 *        {"id": "<csv row id>", "where": "post_content" | "postmeta:<key>#<meta_id>" | "featured_image",
 *         "post_id": 123, "attachment_id": 456 (featured only), "src_path": "/wp-content/uploads/2019/05/x.jpg",
 *         "new_alt": "text"} ]}
 *
 * post_content / postmeta: every <img> in that post (or that meta row) whose src path equals src_path gets
 * alt="new_alt": an existing alt attribute is replaced, a missing one is inserted right after "<img".
 * The host part of src is ignored, so a CSV built on staging applies to live. wp_update_post keeps a revision;
 * postmeta is written by meta_id. featured_image: _wp_attachment_image_alt on the attachment.
 * Output after ===JSON===: one result per row with before/after and whether it was written.
 */
if (!defined('APPLY_ALT_JOB')) { fwrite(STDERR, "no job\n"); exit(1); }
global $wpdb, $job, $mode;
$job = json_decode(APPLY_ALT_JOB, true);
$mode = $job['mode'] ?? 'dry';

function path_of($u) { $u = html_entity_decode($u); return preg_replace('~^(?:https?:)?//[^/]+~i', '', strtok($u, '?')); }

/** Set alt on every <img> whose src path matches. Returns [new_html, changes[]]. */
function set_alt($html, $src_path, $alt) {
    $changes = [];
    $new = preg_replace_callback('~<img\b[^>]*>~i', function ($m) use ($src_path, $alt, &$changes) {
        $tag = $m[0];
        if (!preg_match('~\bsrc\s*=\s*(["\'])([^"\']+)\1~i', $tag, $s) || path_of($s[2]) !== $src_path) return $tag;
        $esc = esc_attr($alt);
        if (preg_match('~\balt\s*=\s*(["\']).*?\1~is', $tag)) {
            $out = preg_replace('~\balt\s*=\s*(["\']).*?\1~is', 'alt="' . $esc . '"', $tag, 1);
        } else {
            $out = preg_replace('~^<img\b~i', '<img alt="' . $esc . '"', $tag, 1);
        }
        if ($out !== $tag) $changes[] = ['before' => $tag, 'after' => $out];
        return $out;
    }, $html);
    return [$new, $changes];
}

$results = [];
foreach ($job['rows'] as $r) {
    $res = ['id' => $r['id'], 'where' => $r['where'], 'post_id' => $r['post_id'], 'changes' => [], 'applied' => null, 'note' => ''];
    $alt = trim((string) $r['new_alt']);
    if ($alt === '') { $res['note'] = 'empty new_alt, skipped'; $results[] = $res; continue; }

    if ($r['where'] === 'featured_image') {
        $aid = (int) $r['attachment_id'];
        $before = (string) get_post_meta($aid, '_wp_attachment_image_alt', true);
        $res['changes'][] = ['before' => $before, 'after' => $alt];
        if ($before === $alt) { $res['note'] = 'already set'; $res['applied'] = false; }
        elseif ($mode === 'apply') { $res['applied'] = (bool) update_post_meta($aid, '_wp_attachment_image_alt', $alt); }
    } elseif ($r['where'] === 'post_content') {
        $p = get_post((int) $r['post_id']);
        if (!$p) { $res['note'] = 'post not found'; $results[] = $res; continue; }
        [$new, $changes] = set_alt($p->post_content, $r['src_path'], $alt);
        $res['changes'] = $changes;
        if (!$changes) $res['note'] = 'no <img> with that src found (already set, or content changed since the probe)';
        elseif ($mode === 'apply') {
            $ok = wp_update_post(['ID' => $p->ID, 'post_content' => $new], true);
            $res['applied'] = !is_wp_error($ok); if (is_wp_error($ok)) $res['note'] = 'ERROR ' . $ok->get_error_message();
        }
    } elseif (preg_match('~^postmeta:(.+)#(\d+)$~', $r['where'], $m)) {
        $meta_id = (int) $m[2];
        $row = $wpdb->get_row($wpdb->prepare("SELECT meta_id, post_id, meta_key, meta_value FROM $wpdb->postmeta WHERE meta_id=%d", $meta_id));
        if (!$row) { $res['note'] = 'meta row not found'; $results[] = $res; continue; }
        [$new, $changes] = set_alt($row->meta_value, $r['src_path'], $alt);
        $res['changes'] = $changes;
        if (!$changes) $res['note'] = 'no <img> with that src in this meta row';
        elseif ($mode === 'apply') {
            $res['applied'] = (bool) $wpdb->update($wpdb->postmeta, ['meta_value' => $new], ['meta_id' => $meta_id]);
            wp_cache_delete($row->post_id, 'post_meta');
        }
    } else {
        $res['note'] = 'unknown where';
    }
    $results[] = $res;
}
echo "===JSON===\n" . json_encode(['home_host' => parse_url(home_url(), PHP_URL_HOST), 'results' => $results], JSON_UNESCAPED_SLASHES);
