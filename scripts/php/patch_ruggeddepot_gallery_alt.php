<?php
/**
 * One-off theme patch for ruggeddepot (theme ruggeddepotoverhaul): the product gallery in inc/woo-custom.php
 * mapped attachment IDs to URLs and printed alt="#". Keep the ID, print the attachment alt, fall back to the
 * product title. Run inside WordPress: wp eval-file scripts/php/patch_ruggeddepot_gallery_alt.php
 * Idempotent; writes woo-custom.php.bak-<date> before changing anything.
 */
$f = get_template_directory() . '/inc/woo-custom.php';
if (!file_exists($f)) { echo "not found: $f\n"; exit(1); }
$src = file_get_contents($f);
if (strpos($src, 'alt="#"') === false) { echo "already patched (no alt=\"#\" in woo-custom.php)\n"; exit(0); }

$map_re = '~\$image_urls\s*=\s*array_map\(\s*function\s*\(\s*\$id\s*\)\s*\{\s*return\s+wp_get_attachment_image_url\(\s*\$id\s*,\s*[\'"]large[\'"]\s*\)\s*;\s*\}\s*,\s*\$image_ids\s*\)\s*;~s';
$new_map = <<<'PHP'
$image_urls = array_map(function ($id) use ($product) {
		$alt = trim((string) get_post_meta($id, '_wp_attachment_image_alt', true));
		if ($alt === '' || $alt === '#') $alt = $product->get_name();
		return ['url' => wp_get_attachment_image_url($id, 'large'), 'alt' => $alt];
	}, $image_ids);
PHP;
$img_re = '~<img\s+class=""\s+src="<\?php\s+echo\s+\$image_url\s*\?>"\s+alt="#">~';
$new_img = '<img class="" src="<?php echo esc_url($image_url[\'url\']) ?>" alt="<?php echo esc_attr($image_url[\'alt\']) ?>">';

if (!preg_match($map_re, $src)) { echo "map block not found as expected; patch by hand\n"; exit(1); }
$n = preg_match_all($img_re, $src);
if ($n !== 2) { echo "expected 2 img tags with alt=\"#\", found $n; patch by hand\n"; exit(1); }
$out = preg_replace($map_re, $new_map, $src, 1);
$out = preg_replace($img_re, $new_img, $out);
$bak = $f . '.bak-' . date('Ymd-His');
copy($f, $bak);
file_put_contents($f, $out);
echo "patched $f (backup $bak): map block + $n img tags\n";
exec('php -l ' . escapeshellarg($f) . ' 2>&1', $lint, $code);
echo implode("\n", $lint), "\n";
if ($code !== 0) { copy($bak, $f); echo "LINT FAILED, restored from backup\n"; exit(1); }
