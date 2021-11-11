FROM rokkie/apache

MAINTAINER Rocco Bruyn <rocco.bruyn@gmail.com>

# Install packages
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        curl \        
        libapache2-mod-php5 \
        libmemcached10 \        
        libssh2-1 \        
        libssh2-php \        
        php5-curl \
        php5-gd \
        php5-intl \
        php5-json \
        php5-mcrypt \
        php5-memcached \
        php5-mysqlnd \
        php5-pgsql \
        php5-readline \
        php5-sqlite && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Add info file 
ADD info.php /var/www/html/info.php

