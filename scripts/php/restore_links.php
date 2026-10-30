<?php
/**
 * Restore posts and postmeta from a fix-redirect-links backup. Runs via `wp eval-file -`; the Python runner
 * prepends the job as RESTORE_LINKS_JOB: {"mode":"dry"|"apply","posts":[{"id":..,"before":..,"after":..}],
 * "meta":[{"meta_id":..,"before":..,"after":..}]}
 *
 * A row is restored only when its CURRENT value equals the backup's `after` (i.e. it still holds what the fix wrote).
 * A row that changed since the fix is reported as "modified since" and left alone; a row already equal to `before`
 * is reported as "already restored". Posts are written directly (no new revision, no save_post hooks).
 */
if (!defined('RESTORE_LINKS_JOB')) { fwrite(STDERR, "no job\n"); exit(1); }
global $wpdb;
$job = json_decode(RESTORE_LINKS_JOB, true);
$mode = $job['mode'] ?? 'dry';
$force = !empty($job['force']);   // restore even when the current value is not what the fix wrote
$out = ['mode' => $mode, 'posts' => [], 'meta' => []];

foreach ($job['posts'] ?? [] as $p) {
    $cur = $wpdb->get_var($wpdb->prepare("SELECT post_content FROM {$wpdb->posts} WHERE ID = %d", $p['id']));
    $e = ['id' => (int)$p['id']];
    if ($cur === null) $e['result'] = 'missing';
    elseif ($cur === $p['before']) $e['result'] = 'already restored';
    elseif ($cur !== ($p['after'] ?? null) && !$force) $e['result'] = 'modified since; left alone';
    else {
        if ($cur !== ($p['after'] ?? null)) $e['forced'] = true;
        if ($mode === 'apply') {
            $ok = $wpdb->update($wpdb->posts, ['post_content' => $p['before']], ['ID' => $p['id']]);
            clean_post_cache($p['id']);
            $e['result'] = $ok === false ? 'ERROR: ' . $wpdb->last_error : (empty($e['forced']) ? 'restored' : 'restored (forced over a later change)');
        } else $e['result'] = 'would restore';
    }
    $out['posts'][] = $e;
}
foreach ($job['meta'] ?? [] as $m) {
    $row = $wpdb->get_row($wpdb->prepare("SELECT meta_value, post_id FROM {$wpdb->postmeta} WHERE meta_id = %d", $m['meta_id']));
    $e = ['meta_id' => (int)$m['meta_id']];
    if (!$row) $e['result'] = 'missing';
    elseif ($row->meta_value === $m['before']) $e['result'] = 'already restored';
    elseif ($row->meta_value !== ($m['after'] ?? null) && !$force) $e['result'] = 'modified since; left alone';
    else {
        if ($row->meta_value !== ($m['after'] ?? null)) $e['forced'] = true;
        if ($mode === 'apply') {
            $ok = $wpdb->update($wpdb->postmeta, ['meta_value' => $m['before']], ['meta_id' => $m['meta_id']]);
            wp_cache_delete($row->post_id, 'post_meta');
            $e['result'] = $ok === false ? 'ERROR: ' . $wpdb->last_error : (empty($e['forced']) ? 'restored' : 'restored (forced over a later change)');
        } else $e['result'] = 'would restore';
    }
    $out['meta'][] = $e;
}
$out['acf_options'] = [];
foreach ($job['acf_options'] ?? [] as $o) {
    $cur = $wpdb->get_var($wpdb->prepare("SELECT option_value FROM {$wpdb->options} WHERE option_id = %d", $o['option_id']));
    $e = ['option_id' => (int)$o['option_id'], 'option_name' => $o['option_name'] ?? ''];
    if ($cur === null) $e['result'] = 'missing';
    elseif ($cur === $o['before']) $e['result'] = 'already restored';
    elseif ($cur !== ($o['after'] ?? null) && !$force) $e['result'] = 'modified since; left alone';
    else {
        if ($cur !== ($o['after'] ?? null)) $e['forced'] = true;
        if ($mode === 'apply') {
            $ok = $wpdb->update($wpdb->options, ['option_value' => $o['before']], ['option_id' => $o['option_id']]);
            if (!empty($o['option_name'])) wp_cache_delete($o['option_name'], 'options'); wp_cache_delete('alloptions', 'options');
            $e['result'] = $ok === false ? 'ERROR: ' . $wpdb->last_error : (empty($e['forced']) ? 'restored' : 'restored (forced over a later change)');
        } else $e['result'] = 'would restore';
    }
    $out['acf_options'][] = $e;
}
echo "\n===JSON===\n" . json_encode($out, JSON_UNESCAPED_SLASHES) . "\n";
