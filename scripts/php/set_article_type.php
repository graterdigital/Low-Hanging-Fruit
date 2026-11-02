<?php
/**
 * Set Yoast's per-post Article schema type on a list of URLs. Run inside WordPress with `wp eval-file`.
 * The job is passed as the ARTICLE_TYPE_JOB constant (JSON): {"mode":"dry|apply","type":"Article","urls":[...]}
 * Prints one JSON object: {"rows":[{"url","id","post_type","title","before","after","status"}]}
 *
 * Yoast reads _yoast_wpseo_schema_article_type; "None" or an empty value means no Article piece. Only posts and pages
 * (and any public custom post type) are touched; a URL that does not resolve to a post is reported as "no post".
 */
if (!defined('ARTICLE_TYPE_JOB')) { fwrite(STDERR, "ARTICLE_TYPE_JOB not defined\n"); exit(1); }
$job  = json_decode(ARTICLE_TYPE_JOB, true);
$mode = $job['mode'] ?? 'dry';
$type = $job['type'] ?? 'Article';
$rows = [];
foreach ($job['urls'] as $url) {
    $row = ['url' => $url, 'id' => 0, 'post_type' => '', 'title' => '', 'before' => '', 'after' => $type, 'status' => ''];
    // Match on path only: the URL comes from Ahrefs with the live hostname, and this may be a staging install.
    $path = parse_url($url, PHP_URL_PATH) ?: '/';
    $id = url_to_postid(home_url($path));
    if (!$id) {
        $slug = trim($path, '/');
        $p = $slug ? get_page_by_path($slug, OBJECT, get_post_types(['public' => true])) : null;
        if ($p) $id = $p->ID;
    }
    if (!$id && !empty($slug)) {
        // last resort: any public post whose post_name is the last path segment
        $last = basename($slug);
        $q = get_posts(['name' => $last, 'post_type' => get_post_types(['public' => true]), 'post_status' => 'publish', 'numberposts' => 1, 'fields' => 'ids']);
        if ($q) $id = $q[0];
    }
    if (!$id) { $row['status'] = 'no post'; $rows[] = $row; continue; }
    $post = get_post($id);
    $row['id'] = $id; $row['post_type'] = $post->post_type; $row['title'] = $post->post_title;
    $row['before'] = (string) get_post_meta($id, '_yoast_wpseo_schema_article_type', true);
    if ($row['before'] === $type) { $row['status'] = 'already'; $rows[] = $row; continue; }
    if ($mode === 'apply') {
        update_post_meta($id, '_yoast_wpseo_schema_article_type', $type);
        $row['status'] = ((string) get_post_meta($id, '_yoast_wpseo_schema_article_type', true) === $type) ? 'set' : 'failed';
    } else {
        $row['status'] = 'would set';
    }
    $rows[] = $row;
}
if ($mode === 'apply' && function_exists('wp_cache_flush')) wp_cache_flush();
echo json_encode(['rows' => $rows], JSON_UNESCAPED_SLASHES);
