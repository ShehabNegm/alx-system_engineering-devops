# pupet script to set client side SSH config file
include stdlib
file_line { 'private key adding':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}

file_line { 'private key adding':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
