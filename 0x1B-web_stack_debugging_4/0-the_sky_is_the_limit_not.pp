# Increase the number of traffic for Nginx

# Update the Ulimit 
exec{'fix--for-nginx':
        command => '/bin/sed -i "s/15/4096/g" /etc/default/nginx',

        path    => '/usr/bin:/usr/sbin:/bin',
}

# Restart the Nginx service

exec{'restart-nginx':
        command => '/etc/init.d/nginx restart',

        path    => '/etc/init.d/',
}
