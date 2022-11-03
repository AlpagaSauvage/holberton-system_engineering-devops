#Install package

exec { 'install flask':
  command => 'sudo pip3 install -Iv flask==2.1.0',
  path    => '/usr/bin'
}
