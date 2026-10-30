<?php
/**
 * Regression test for the rewrite rules in scripts/php/replace_links.php. Run: php scripts/tests/test_replace_links.php
 * Loads only the setup and the rewrite()/rewrite_value()/walk() functions (nothing touches a database).
 */
define('REPLACE_LINKS_JOB', json_encode(["mode" => "dry", "host" => "example.com", "legacy_hosts" => ["www.example.com", "old.wpengine.com"],
    "swaps" => [["old" => "https://example.com/contact", "new" => "https://example.com/contact/"],
                ["old" => "https://example.com/child-support/", "new" => "https://example.com/divorce/child-support/"],
                ["old" => "https://example.com/rep-locator/\\", "new" => "https://example.com/rep-locator/"]]]));
function home_url() { return "https://example.com"; }
$src = file_get_contents(__DIR__ . '/../php/replace_links.php');
$src = substr($src, 0, strpos($src, '/** Anchored find-regex'));
eval(str_replace('<?php', '', $src));

$fail = 0;
function expect($name, $got, $want) { global $fail; $ok = $got === $want; if (!$ok) $fail++; echo ($ok ? "ok   " : "FAIL "), $name, $ok ? "" : "\n     got:  $got\n     want: $want", "\n"; }
function rw($s) { $h = []; return rewrite($s, $h); }
function rv($s) { $h = []; return rewrite_value($s, $h); }

expect("refuses unsafe swap", count($swaps), 2);
expect("html absolute", rw('<a href="https://example.com/contact">'), '<a href="https://example.com/contact/">');
expect("html relative", rw("<a href='/contact'>"), "<a href='/contact/'>");
expect("html anchored: no match inside longer path", rw('<a href="/divorce/child-support/">'), '<a href="/divorce/child-support/">');
expect("html anchored: slashless does not match slashed", rw('<a href="/contact/">'), '<a href="/contact/">');
expect("html www host moved to canonical", rw('<a href="https://www.example.com/fine/">'), '<a href="https://example.com/fine/">');
expect("html legacy host moved", rw('<a href="http://old.wpengine.com/x/">'), '<a href="http://example.com/x/">');
expect("plain json swap", rw('{"url":"https:\/\/example.com\/contact"}'), '{"url":"https:\/\/example.com\/contact\/"}');
expect("plain json relative", rw('{"url":"\/contact"}'), '{"url":"\/contact\/"}');
expect("plain json www host", rw('{"url":"https:\/\/www.example.com\/a\/"}'), '{"url":"https:\/\/example.com\/a\/"}');
expect("double-encoded json swap", rw('"{\"url\":\"https:\/\/example.com\/contact\"}"'), '"{\"url\":\"https:\/\/example.com\/contact\/\"}"');
expect("json stays valid", json_decode(rw('{"a":"https:\/\/example.com\/contact","b":"https:\/\/www.example.com\/c\/"}')) !== null, true);
expect("whole value with fragment", rv("https://example.com/contact#top"), "https://example.com/contact/#top");
expect("whole value with query", rv("/contact?x=1"), "/contact/?x=1");
expect("whole value www kept path", rv("https://www.example.com/other/"), "https://example.com/other/");
expect("serialized walk", serialize(walk(unserialize('a:1:{s:3:"url";s:27:"https://example.com/contact";}'), $h)), 'a:1:{s:3:"url";s:28:"https://example.com/contact/";}');
echo $fail ? "\n$fail FAILED\n" : "\nall passed\n";
exit($fail ? 1 : 0);
