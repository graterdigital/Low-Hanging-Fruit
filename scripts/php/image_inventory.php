<?php
/**
 * Image inventory for fix-images. Runs inside WordPress via `wp eval-file`; the Python runner prepends
 * the job as IMAGE_INVENTORY_JOB. Read-only: this file never writes to the database or the filesystem.
 *
 * Job: {"mode": "inventory", "host": "example.com",
 *       "urls": ["https://example.com/wp-content/uploads/2025/03/big.png", ...],   // oversized files from Ahrefs
 *       "ids": [123, 456]}                                                          // attachment IDs (used by regenerate-prep)
 *
 * Output (after ===JSON===):
 *   env        tools available for compression on the server + PHP image libs + upload dir
 *   webp       WebP Express / other optimizer plugins and their state, as far as the DB shows
 *   files      one row per URL: attachment ID, file path, bytes, mime, width x height, largest registered
 *              sub-size, where it is referenced (posts, postmeta, options counts; thumbnail URLs included)
 *   alt        every <img> in post_content/postmeta with no alt attribute or alt="" (page URL, src, context)
 *   broken     <img> whose src points at this host but whose file is missing on disk (uploads only)
 */
if (!defined('IMAGE_INVENTORY_JOB')) { fwrite(STDERR, "no job\n"); exit(1); }
global $wpdb, $job, $home_host, $live_host, $hosts_re;
$job = json_decode(IMAGE_INVENTORY_JOB, true);
$home_host = parse_url(home_url(), PHP_URL_HOST);
$live_host = $job['host'];
$hosts = array_values(array_unique([$live_host, $home_host]));
$hosts_re = '(?:www\.)?(?:' . implode('|', array_map(fn($h) => preg_quote(preg_replace('~^www\.~', '', $h), '~'), $hosts)) . ')';
$path_of = fn($u) => preg_replace('~^https?://(www\.)?[^/]+~', '', $u);

$up = wp_upload_dir();
$out = ['home_host' => $home_host, 'env' => [], 'webp' => [], 'files' => [], 'alt' => [], 'broken' => []];

// ---- environment: what can compress images here ----------------------------------------------
$which = function ($bin) { $p = trim((string) @shell_exec('command -v ' . escapeshellarg($bin) . ' 2>/dev/null')); return $p ?: null; };
$out['env'] = [
    'uploads_basedir' => $up['basedir'], 'uploads_baseurl' => $up['baseurl'],
    'php' => PHP_VERSION,
    'imagick' => extension_loaded('imagick') ? (new Imagick())->getVersion()['versionString'] : null,
    'gd' => function_exists('gd_info') ? (gd_info()['GD Version'] ?? 'yes') : null,
    'gd_webp' => function_exists('imagewebp'),
    'bin' => ['pngquant' => $which('pngquant'), 'oxipng' => $which('oxipng'), 'optipng' => $which('optipng'),
              'cwebp' => $which('cwebp'), 'jpegoptim' => $which('jpegoptim'), 'convert' => $which('convert'), 'magick' => $which('magick')],
    'big_image_size_threshold' => apply_filters('big_image_size_threshold', 2560, [], 0, 0),
    'registered_sizes' => wp_get_registered_image_subsizes(),
];

// ---- optimizer plugins ---------------------------------------------------------------------
$active = (array) get_option('active_plugins', []);
$known = ['webp-express' => 'webp-express/webp-express.php', 'enable-media-replace' => 'enable-media-replace/enable-media-replace.php',
          'shortpixel' => 'shortpixel-image-optimiser/wp-shortpixel.php', 'smush' => 'wp-smushit/wp-smush.php',
          'ewww' => 'ewww-image-optimizer/ewww-image-optimizer.php', 'imagify' => 'imagify/imagify.php', 'optimole' => 'optimole-wp/optimole-wp.php',
          'litespeed' => 'litespeed-cache/litespeed-cache.php', 'converter-for-media' => 'webp-converter-for-media/webp-converter-for-media.php'];
foreach ($known as $k => $file) $out['webp'][$k] = in_array($file, $active, true) ? 'active' : (file_exists(WP_PLUGIN_DIR . '/' . $file) ? 'installed-inactive' : 'absent');
if ($out['webp']['webp-express'] === 'active') {
    $cfg = WP_CONTENT_DIR . '/webp-express/config/config.json';
    $c = file_exists($cfg) ? json_decode(file_get_contents($cfg), true) : null;
    $out['webp']['webp-express-config'] = $c ? array_intersect_key($c, array_flip(['operation-mode', 'image-types', 'destination-folder', 'destination-extension',
        'redirect-to-existing-in-htaccess', 'enable-redirection-to-converter', 'alter-html', 'alter-html-only-for-webp-enabled-browsers', 'quality-auto', 'max-quality', 'converters'])) : 'config.json not found';
    $webps = 0; $dir = WP_CONTENT_DIR . '/webp-express/webp-images';
    if (is_dir($dir)) foreach (new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir, FilesystemIterator::SKIP_DOTS)) as $f) if (substr($f, -5) === '.webp') $webps++;
    // also count sibling .webp next to originals (destination-folder "mingled")
    $sib = 0;
    foreach (new RecursiveIteratorIterator(new RecursiveDirectoryIterator($up['basedir'], FilesystemIterator::SKIP_DOTS)) as $f) if (substr($f, -5) === '.webp') $sib++;
    $out['webp']['webp-express-converted-files'] = ['separate-folder' => $webps, 'mingled-in-uploads' => $sib];
}

// ---- reference counting helpers ------------------------------------------------------------
function like_count($table, $col, $needle, $extra = '') {
    global $wpdb;
    return (int) $wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM $table WHERE $col LIKE %s $extra", '%' . $wpdb->esc_like($needle) . '%'));
}

// ---- per-file inventory ----------------------------------------------------------------------
foreach ($job['urls'] ?? [] as $url) {
    $path = $path_of($url);
    $row = ['url' => $url, 'path' => $path, 'attachment_id' => null, 'file' => null, 'bytes' => null, 'mime' => null,
            'width' => null, 'height' => null, 'is_scaled_variant' => (bool) preg_match('~-scaled\.\w+$~', $path),
            'refs' => ['post_content' => 0, 'postmeta' => 0, 'options' => 0, 'thumbnail_refs' => 0], 'sizes' => []];
    $id = attachment_url_to_postid($url);
    if (!$id) { // staging host differs from the live host in guid/metadata; try on the current host
        $id = attachment_url_to_postid(home_url($path));
    }
    if (!$id) { // last resort: match the relative upload path in _wp_attached_file
        $rel = ltrim(preg_replace('~^.*?/uploads/~', '', $path), '/');
        $id = (int) $wpdb->get_var($wpdb->prepare("SELECT post_id FROM $wpdb->postmeta WHERE meta_key='_wp_attached_file' AND meta_value=%s LIMIT 1", $rel));
    }
    if ($id) {
        $row['attachment_id'] = $id;
        $file = get_attached_file($id);
        $row['file'] = $file;
        $row['mime'] = get_post_mime_type($id);
        $meta = wp_get_attachment_metadata($id) ?: [];
        $row['width'] = $meta['width'] ?? null; $row['height'] = $meta['height'] ?? null;
        $row['original_image'] = $meta['original_image'] ?? null;   // set when WP already made a -scaled copy
        foreach (($meta['sizes'] ?? []) as $name => $s) {
            $sf = dirname($file) . '/' . $s['file'];
            $row['sizes'][$name] = ['file' => $s['file'], 'w' => $s['width'], 'h' => $s['height'], 'bytes' => file_exists($sf) ? filesize($sf) : null];
        }
        if ($file && file_exists($file)) $row['bytes'] = filesize($file);
        $row['is_featured_image_of'] = (int) $wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM $wpdb->postmeta WHERE meta_key='_thumbnail_id' AND meta_value=%s", (string) $id));
        $row['in_acf_image_fields'] = (int) $wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM $wpdb->postmeta WHERE meta_key NOT LIKE '\_%' AND meta_value=%s", (string) $id));
    } else {
        $abs = $up['basedir'] . preg_replace('~^.*?/uploads~', '', $path);
        if (file_exists($abs)) { $row['file'] = $abs; $row['bytes'] = filesize($abs); $info = @getimagesize($abs); if ($info) { $row['width'] = $info[0]; $row['height'] = $info[1]; $row['mime'] = $info['mime']; } }
    }
    // references by URL path (any host), including -WxH thumbnail variants
    $stem = preg_replace('~\.(\w+)$~', '', $path); $ext = pathinfo($path, PATHINFO_EXTENSION);
    $row['refs']['post_content'] = like_count($wpdb->posts, 'post_content', $path, "AND post_type NOT IN ('revision','attachment')");
    $row['refs']['postmeta'] = like_count($wpdb->postmeta, 'meta_value', $path, "AND meta_key NOT IN ('_wp_attached_file','_wp_attachment_metadata')");
    $row['refs']['options'] = like_count($wpdb->options, 'option_value', $path, "AND option_name NOT LIKE '\_transient%' AND option_name NOT LIKE '\_site\_transient%'");
    $row['refs']['thumbnail_refs'] = (int) $wpdb->get_var($wpdb->prepare(
        "SELECT (SELECT COUNT(*) FROM $wpdb->posts WHERE post_type NOT IN ('revision','attachment') AND post_content REGEXP %s)
              + (SELECT COUNT(*) FROM $wpdb->postmeta WHERE meta_key NOT IN ('_wp_attached_file','_wp_attachment_metadata') AND meta_value REGEXP %s)",
        preg_quote($stem) . '-[0-9]+x[0-9]+\\.' . $ext, preg_quote($stem) . '-[0-9]+x[0-9]+\\.' . $ext));
    $out['files'][] = $row;
}

// ---- alt text scan: every <img> without alt, or alt="" ------------------------------------------
function scan_imgs($html, $where, $post_id, &$alt, &$broken) {
    global $hosts_re; static $up = null; if ($up === null) $up = wp_upload_dir();
    if (stripos($html, '<img') === false) return;
    if (!preg_match_all('~<img\b[^>]*>~i', $html, $m)) return;
    foreach ($m[0] as $tag) {
        $src = preg_match('~\bsrc\s*=\s*["\']([^"\']+)~i', $tag, $s) ? html_entity_decode($s[1]) : '';
        $has_alt = preg_match('~\balt\s*=\s*(["\'])(.*?)\1~is', $tag, $a);
        $alt_val = $has_alt ? trim($a[2]) : null;
        $junk = $has_alt && $alt_val !== '' && (mb_strlen($alt_val) <= 2 || preg_match('~^(?:[\W_]+|\d+|image|img|photo|picture|pic|untitled|n/?a|none|null|alt|logo|placeholder|(?:img|image|dsc|photo|pic|screenshot)[_ -]?\d+)$~i', $alt_val) || preg_match('~\.(jpe?g|png|gif|webp|avif|svg)$~i', $alt_val));
        if (!$has_alt || $alt_val === '' || $junk) {
            $alt[] = ['post_id' => $post_id, 'where' => $where, 'src' => $src, 'alt' => $has_alt ? $alt_val : null, 'tag' => mb_substr($tag, 0, 300)];
        }
        if ($src && preg_match('~^(?:https?:)?//' . $hosts_re . '(/wp-content/uploads/.+)$~i', $src, $u)) {
            $abs = $up['basedir'] . preg_replace('~^.*?/uploads~', '', strtok($u[1], '?'));
            if (!file_exists($abs)) $broken[] = ['post_id' => $post_id, 'where' => $where, 'src' => $src];
        }
    }
}
// Only public-facing content: revisions, builder templates, TablePress tables, menus, ACF definitions etc. never render as a page.
$public_types = array_values(array_filter(get_post_types(['public' => true]), fn($t) => $t !== 'attachment'));
$types_sql = implode(',', array_map(fn($t) => $wpdb->prepare('%s', $t), $public_types));
$out['scanned_post_types'] = $public_types;
$posts = $wpdb->get_results("SELECT ID, post_type, post_status, post_content FROM $wpdb->posts WHERE post_type IN ($types_sql) AND post_status IN ('publish','private','draft','future') AND post_content LIKE '%<img%'");
foreach ($posts as $p) scan_imgs($p->post_content, 'post_content', (int) $p->ID, $out['alt'], $out['broken']);
$metas = $wpdb->get_results("SELECT pm.meta_id, pm.post_id, pm.meta_key, pm.meta_value FROM $wpdb->postmeta pm JOIN $wpdb->posts p ON p.ID = pm.post_id
    WHERE p.post_type IN ($types_sql) AND p.post_status IN ('publish','private','draft','future') AND pm.meta_key NOT LIKE '\_%' AND pm.meta_value LIKE '%<img%'");
foreach ($metas as $mm) scan_imgs($mm->meta_value, "postmeta:{$mm->meta_key}#{$mm->meta_id}", (int) $mm->post_id, $out['alt'], $out['broken']);
// attachments whose own alt is empty but which are used as featured images on indexable post types
$noalt = $wpdb->get_results("SELECT pm.post_id AS attachment_id, pm.meta_value AS used_by FROM $wpdb->postmeta pm JOIN $wpdb->posts p ON p.ID = pm.post_id
    WHERE pm.meta_key='_thumbnail_id' AND p.post_type IN ($types_sql) AND p.post_status IN ('publish','private','draft','future')
      AND NOT EXISTS (SELECT 1 FROM $wpdb->postmeta a WHERE a.post_id = pm.meta_value AND a.meta_key='_wp_attachment_image_alt' AND a.meta_value <> '')");
foreach ($noalt as $r) $out['alt'][] = ['post_id' => (int) $r->attachment_id, 'where' => 'featured_image(attachment ' . $r->used_by . ')', 'src' => wp_get_attachment_url((int) $r->used_by), 'alt' => null, 'tag' => '_wp_attachment_image_alt empty'];
foreach ($out['alt'] as &$a) { $a['page_url'] = get_permalink($a['post_id']) ?: null; $a['post_type'] = get_post_type($a['post_id']) ?: null; $a['post_status'] = get_post_status($a['post_id']) ?: null; $a['title'] = html_entity_decode(get_the_title($a['post_id']));
    // tier: A = alt attribute absent on a published page (what Ahrefs counts); B = alt="" inline (decorative by HTML rules, often just unfilled); C = featured image whose attachment has no alt; D = not published
    $a['tier'] = $a['post_status'] !== 'publish' ? 'D' : (strpos($a['where'], 'featured_image') === 0 ? 'C' : ($a['alt'] === null ? 'A' : 'B')); }
unset($a);
foreach ($out['broken'] as &$b) { $b['page_url'] = get_permalink($b['post_id']) ?: null; }
unset($b);

// ---- WooCommerce products: featured + gallery + variation images (for the title-derived alt rule) --------------
$out['products'] = [];
if (post_type_exists('product')) {
    $prods = $wpdb->get_results("SELECT ID, post_title FROM $wpdb->posts WHERE post_type='product' AND post_status IN ('publish','private') ORDER BY ID");
    $alt_of = function ($aid) use ($wpdb) { return (string) $wpdb->get_var($wpdb->prepare("SELECT meta_value FROM $wpdb->postmeta WHERE post_id=%d AND meta_key='_wp_attachment_image_alt'", $aid)); };
    foreach ($prods as $pr) {
        $feat = (int) get_post_meta($pr->ID, '_thumbnail_id', true);
        $gal = array_values(array_filter(array_map('intval', explode(',', (string) get_post_meta($pr->ID, '_product_image_gallery', true)))));
        $vars = $wpdb->get_results($wpdb->prepare("SELECT ID, post_excerpt FROM $wpdb->posts WHERE post_type='product_variation' AND post_parent=%d AND post_status='publish'", $pr->ID));
        $images = [];
        if ($feat) $images[] = ['attachment_id' => $feat, 'role' => 'featured', 'file' => basename((string) get_post_meta($feat, '_wp_attached_file', true)), 'alt' => $alt_of($feat)];
        foreach ($gal as $i => $g) $images[] = ['attachment_id' => $g, 'role' => 'gallery', 'index' => $i + 1, 'file' => basename((string) get_post_meta($g, '_wp_attached_file', true)), 'alt' => $alt_of($g)];
        foreach ($vars as $v) { $vt = (int) get_post_meta($v->ID, '_thumbnail_id', true); if ($vt && $vt !== $feat && !in_array($vt, $gal, true))
            $images[] = ['attachment_id' => $vt, 'role' => 'variation', 'variation' => trim((string) $v->post_excerpt), 'file' => basename((string) get_post_meta($vt, '_wp_attached_file', true)), 'alt' => $alt_of($vt)]; }
        if ($images) $out['products'][] = ['id' => (int) $pr->ID, 'title' => html_entity_decode($pr->post_title), 'url' => get_permalink($pr->ID), 'images' => $images];
    }
}
echo "===JSON===\n" . json_encode($out, JSON_UNESCAPED_SLASHES);
