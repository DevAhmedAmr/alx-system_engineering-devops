#!/usr/bin/pup
# Install flask 2.1.0

package { 'python3-pip':
  ensure => installed,
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package {'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
