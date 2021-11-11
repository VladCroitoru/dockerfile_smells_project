FROM debian:jessie

MAINTAINER "Dylan Miles" <dylan.g.miles@gmail.com>

# Install PHP-FPM and popular/laravel required extensions
RUN apt-get update -y && \
    apt-get install -y \
    php5-fpm \
    php5-curl \
    php5-gd \
    php5-geoip \
    php5-imagick \
    php5-imap \
    php5-json \
    php5-ldap \
    php5-mcrypt \
    php5-memcache \
    php5-memcached \
    php5-mongo \
    php5-mssql \
    php5-mysqlnd \
    php5-pgsql \
    php5-redis \
    php5-sqlite \
    php5-xdebug \
    php5-xmlrpc \
    php5-xcache \
    php5-tidy \
    php5-Intl \
    php-pear


# Install pear mail for some legacy applications
RUN     pear install mail     \
    &&  pear install Net_SMTP

#Patch pear mail to allow for certificate exceptions
RUN sed -i "s/\$this->_socket_options = \$socket_options;/\$this->_socket_options = array('ssl' => array('verify_peer' => false, 'verify_peer_name' => false, 'allow_self_signed' => true));/" /usr/share/php/Net/SMTP.php


# Configure PHP-FPM
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/fpm/php.ini && \
    sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini && \
    sed -i "s/display_errors = Off/display_errors = stderr/" /etc/php5/fpm/php.ini && \
    sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 30M/" /etc/php5/fpm/php.ini && \
    sed -i "s/post_max_size = 8M/post_max_size = 30M/" /etc/php5/fpm/php.ini && \
    sed -i "s/;opcache.enable=0/opcache.enable=1/" /etc/php5/fpm/php.ini && \
    sed -i "s/;opcache.memory_consumption=64/opcache.memory_consumption=128/" /etc/php5/fpm/php.ini && \
    sed -i "s/;opcache.max_accelerated_files=2000/opcache.max_accelerated_files=8000/" /etc/php5/fpm/php.ini && \
    sed -i "s/;opcache.revalidate_freq=2/opcache.revalidate_freq=60/" /etc/php5/fpm/php.ini && \
    sed -i "s/;opcache.use_cwd=1/opcache.use_cwd=1/" /etc/php5/fpm/php.ini && \
    sed -i "s/;opcache.validate_timestamps=1/opcache.validate_timestamps=1/" /etc/php5/fpm/php.ini && \
    sed -i "s/;opcache.save_comments=1/opcache.save_comments=1/" /etc/php5/fpm/php.ini && \
    sed -i "s/;opcache.enable_file_override=0/opcache.enable_file_override=0/" /etc/php5/fpm/php.ini && \
    sed -i "s/max_execution_time = 30/max_execution_time = 300/" /etc/php5/fpm/php.ini && \
    sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf && \
    sed -i '/^listen = /clisten = 9000' /etc/php5/fpm/pool.d/www.conf && \
    sed -i '/^listen.allowed_clients/c;listen.allowed_clients =' /etc/php5/fpm/pool.d/www.conf && \
    sed -i '/^;catch_workers_output/ccatch_workers_output = yes' /etc/php5/fpm/pool.d/www.conf && \
    sed -i '/^;env\[TEMP\] = .*/aenv[DB_PORT_3306_TCP_ADDR] = $DB_PORT_3306_TCP_ADDR' /etc/php5/fpm/pool.d/www.conf

# Configure XDebug
#RUN   echo "xdebug.remote_enable = 1" >> /etc/php5/fpm/conf.d/20-xdebug.ini
#RUN   echo "xdebug.remote_connect_back = 1" >> /etc/php5/fpm/conf.d/20-xdebug.ini
#RUN   echo "xdebug.remote_port = 9000" >> /etc/php5/fpm/conf.d/20-xdebug.ini

RUN mkdir -p /data
VOLUME ["/data"]

EXPOSE 9000

ENTRYPOINT ["/usr/sbin/php5-fpm", "-F"]
