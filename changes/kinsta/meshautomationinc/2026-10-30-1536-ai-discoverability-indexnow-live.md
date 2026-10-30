# ai-discoverability: IndexNow plugin on meshautomationinc.com (live)

Run 2026-10-30-1536 · alias `meshautomationinc` · result **installed** · IndexNow (Microsoft Bing, free)

Rollback: `wp plugin deactivate indexnow && wp plugin delete indexnow` on the same alias. The plugin generates a new key on every activation.

```
PHP Notice:  Constant WP_CACHE already defined in phar:///usr/local/bin/wp/vendor/wp-cli/wp-cli/php/WP_CLI/Runner.php(1334) : eval()'d code on line 57
Notice: Constant DISALLOW_FILE_EDIT already defined in /www/meshautomation_374/public/wp-content/themes/mesh/functions.php on line 99
Notice: Function _load_textdomain_just_in_time was called <strong>incorrectly</strong>. Translation loading for the <code>acf</code> domain was triggered too early. This is usually an indicator for some code in the plugin or theme running too early. Translations should be loaded at the <code>init</code> action or later. Please see <a href="https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/">Debugging in WordPress</a> for more information. (This message was added in version 6.7.0.) in /www/meshautomation_374/public/wp-includes/functions.php on line 6260
Installing IndexNow Plugin (1.0.4)
Downloading installation package from https://downloads.wordpress.org/plugin/indexnow.zip...
Unpacking the package...
Installing the plugin...
Plugin installed successfully.
Activating 'indexnow'...
Plugin 'indexnow' activated.
Success: Installed 1 of 1 plugins.
RC=0
```
