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
    $id = url_to_postid($url);
    if (!$id) {
        // url_to_postid misses some rewrites; try the path as a page slug chain
        $path = trim(parse_url($url, PHP_URL_PATH), '/');
        $p = $path ? get_page_by_path($path, OBJECT, get_post_types(['public' => true])) : null;
        if ($p) $id = $p->ID;
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
