<?php
/**
 * Write Yoast SEO titles and meta descriptions on a list of URLs. Run inside WordPress with `wp eval-file -`.
 * The job is passed as the META_JOB constant (JSON):
 *   {"mode":"dry|apply","rows":[{"url":"https://site/path/","title":"...","description":"..."}]}
 * An empty "title" or "description" means "leave that field alone".
 * Prints one JSON object after a ===JSON=== marker:
 *   {"seo_plugin":"yoast","rows":[{"url","id","post_type","post_title","title_before","title_after","description_before",
 *     "description_after","rendered_title","rendered_description","status"}]}
 *
 * Yoast reads _yoast_wpseo_title and _yoast_wpseo_metadesc straight from postmeta (no cache of its own; the runner flushes
 * the object and page caches afterwards). rendered_* come from YoastSEO()->meta->for_post(), i.e. the <title> and
 * <meta name="description"> Yoast will actually output: in dry mode that is the current state, after an apply the new one,
 * so the log shows whether Yoast appended its separator/brand from the template or used the literal text.
 *
 * URL matching is on the path only (the URL comes from Ahrefs with the live hostname and this may be a staging install),
 * the same three-step lookup as set_article_type.php. A URL that does not resolve to a post is reported as "no post".
 * Only Yoast is supported here; the runner refuses other SEO plugins before shipping this file.
 */
if (!defined('META_JOB')) { fwrite(STDERR, "META_JOB not defined\n"); exit(1); }
$job  = json_decode(META_JOB, true);
$mode = $job['mode'] ?? 'dry';
$rows = [];

function lhf_meta_resolve_post($url) {
    $path = parse_url($url, PHP_URL_PATH) ?: '/';
    if ($path === '/') {
        $front = (int) get_option('page_on_front');
        return $front ?: 0;   // a posts-page front has no post to carry meta; Yoast's homepage template rules it
    }
    $id = url_to_postid(home_url($path));
    $slug = trim($path, '/');
    if (!$id && $slug) {
        $p = get_page_by_path($slug, OBJECT, get_post_types(['public' => true]));
        if ($p) $id = $p->ID;
    }
    if (!$id && $slug) {
        $q = get_posts(['name' => basename($slug), 'post_type' => get_post_types(['public' => true]), 'post_status' => 'publish', 'numberposts' => 1, 'fields' => 'ids']);
        if ($q) $id = $q[0];
    }
    return (int) $id;
}

function lhf_meta_rendered($id) {
    if (!function_exists('YoastSEO')) return ['', ''];
    try {
        $m = YoastSEO()->meta->for_post($id);
        if (!$m) return ['', ''];
        return [(string) $m->title, (string) $m->description];
    } catch (\Throwable $e) { return ['', '']; }
}

foreach ($job['rows'] as $in) {
    $url = $in['url'] ?? '';
    $want_t = trim((string) ($in['title'] ?? ''));
    $want_d = trim((string) ($in['description'] ?? ''));
    $row = ['url' => $url, 'id' => 0, 'post_type' => '', 'post_title' => '', 'title_before' => '', 'title_after' => '',
            'description_before' => '', 'description_after' => '', 'rendered_title' => '', 'rendered_description' => '', 'status' => ''];
    if ($want_t === '' && $want_d === '') { $row['status'] = 'nothing to write'; $rows[] = $row; continue; }
    $id = lhf_meta_resolve_post($url);
    if (!$id) { $row['status'] = 'no post'; $rows[] = $row; continue; }
    $post = get_post($id);
    if (!$post || $post->post_status !== 'publish') { $row['id'] = $id; $row['status'] = 'not published'; $rows[] = $row; continue; }
    $row['id'] = $id; $row['post_type'] = $post->post_type; $row['post_title'] = $post->post_title;
    $row['title_before'] = (string) get_post_meta($id, '_yoast_wpseo_title', true);
    $row['description_before'] = (string) get_post_meta($id, '_yoast_wpseo_metadesc', true);
    $row['title_after'] = $want_t !== '' ? $want_t : $row['title_before'];
    $row['description_after'] = $want_d !== '' ? $want_d : $row['description_before'];
    $changed = ($row['title_after'] !== $row['title_before']) || ($row['description_after'] !== $row['description_before']);
    if (!$changed) {
        $row['status'] = 'already';
    } elseif ($mode === 'apply') {
        if ($want_t !== '') update_post_meta($id, '_yoast_wpseo_title', $want_t);
        if ($want_d !== '') update_post_meta($id, '_yoast_wpseo_metadesc', $want_d);
        clean_post_cache($id);
        $ok_t = $want_t === '' || (string) get_post_meta($id, '_yoast_wpseo_title', true) === $want_t;
        $ok_d = $want_d === '' || (string) get_post_meta($id, '_yoast_wpseo_metadesc', true) === $want_d;
        $row['status'] = ($ok_t && $ok_d) ? 'set' : 'failed';
    } else {
        $row['status'] = 'would set';
    }
    // Yoast caches its indexable rows; after an apply, rebuild this post's so rendered_* reflect the new meta.
    if ($mode === 'apply' && $row['status'] === 'set' && function_exists('YoastSEO')) {
        try { do_action('wpseo_save_indexable', $id); } catch (\Throwable $e) {}
        try {
            $c = YoastSEO()->classes->get('Yoast\\WP\\SEO\\Repositories\\Indexable_Repository');
            if ($c && method_exists($c, 'find_by_id_and_type')) {
                $ix = $c->find_by_id_and_type($id, 'post', false);
                if ($ix) { $b = YoastSEO()->classes->get('Yoast\\WP\\SEO\\Builders\\Indexable_Builder'); if ($b) $b->build_for_id_and_type($id, 'post', $ix); }
            }
        } catch (\Throwable $e) {}
    }
    [$row['rendered_title'], $row['rendered_description']] = lhf_meta_rendered($id);
    $rows[] = $row;
}
if ($mode === 'apply' && function_exists('wp_cache_flush')) wp_cache_flush();
$plugin = (defined('WPSEO_VERSION') ? 'yoast' : (function_exists('aioseo') ? 'aioseo' : 'unknown'));
echo "===JSON===" . json_encode(['seo_plugin' => $plugin, 'rows' => $rows], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
