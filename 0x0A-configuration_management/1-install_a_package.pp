# Install a package
exec { 'puppet-lint'
  command => 'sudo apt-get install puppet-lint@2.5.0',
}
