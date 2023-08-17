# fix user ulimit
exec{'replace5':
  provider => shell,
  command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace4'],
}

exec{'replace4':
  provider => shell,
  command  => 'sudo sed -i "s/holberton soft nofile 4/holberton soft nofile 40000/" /etc/security/limits.conf',
}
