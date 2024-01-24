# A resource declaration
file {'/tmp/school':
ensure => 'file',
path => '/tmp/codingschool',
content => "I love Puppet",
owner => 'www-data',
group => 'www-data',
mode => '0744',
}