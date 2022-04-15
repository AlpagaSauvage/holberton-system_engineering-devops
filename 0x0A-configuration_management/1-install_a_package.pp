# Install a package
exec { 'puppet-lint'
  command => 'sudo gem install puppet-lint -v 2.5.0',
  path    => ['/usr/bin'],
}
