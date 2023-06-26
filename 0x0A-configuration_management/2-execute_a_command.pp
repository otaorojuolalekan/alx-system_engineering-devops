# executes a pkill on 'killmenow' process using Puppet

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
