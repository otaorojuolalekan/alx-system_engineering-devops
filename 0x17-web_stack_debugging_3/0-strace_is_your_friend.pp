# problem: phpp instead of php in wp-settings.php bad `phpp` extensions to `php`

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
