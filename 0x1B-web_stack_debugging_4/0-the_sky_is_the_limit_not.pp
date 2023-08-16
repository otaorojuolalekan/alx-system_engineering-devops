# fix nginx ulimit
$ulimit = 4096
file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT=${ulimit}",
  before => Exec['restart nginx'],
}

exec { 'restart nginx':
  provider => shell,
  command => 'sudo service nginx restart',
}
