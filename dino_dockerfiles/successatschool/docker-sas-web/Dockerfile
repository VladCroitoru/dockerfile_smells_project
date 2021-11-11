FROM php:7.4-apache

# System packages inc. Node + npm
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -

# Deps include some needed for post-npm-install scripts, e.g. imagemin Webpack plugin's gifsicle install.
RUN apt-get update -qq  \
 && apt-get install -y acl build-essential cmake curl git git-core gnupg2 libicu-dev libjpeg62-turbo-dev libmemcached-dev libmemcached11 libmemcachedutil2 libpng-dev libz-dev nodejs ssh vim-tiny wget unzip \
 && rm -rf /var/lib/apt/lists/* /var/cache/apk/*

# Apache configuration
COPY config/ecs.conf /etc/apache2/sites-available/
COPY config/ssl-local.conf /etc/apache2/sites-available/

RUN a2enmod headers \
 && a2enmod remoteip \
 && a2enmod rewrite \
 && a2enmod ssl \
 && a2dissite 000-default \
 && a2ensite ssl-local \
 && echo ServerName localhost >> /etc/apache2/apache2.conf

# Extension config and install
RUN docker-php-ext-configure gd --with-jpeg
RUN docker-php-ext-install bcmath gd intl opcache pcntl pdo_mysql sockets
RUN pecl install memcached && docker-php-ext-enable memcached

# TODO retire memcache extension, once we've replaced the bundle using it with native
# Symfony 3.4 sessions in Production.
# Manual build needed to get memcache extension support on PHP 7.x
# See https://stackoverflow.com/a/48380759/2803757 and https://github.com/LeaseWeb/LswMemcacheBundle#requirements
RUN cd /usr/local/src/ \
 && wget https://github.com/remicollet/pecl-memcache/archive/issue-php73.zip \
 && unzip issue-php73.zip \
 && mv pecl-memcache-issue-php73 pecl-memcache-php7 \
 && cd pecl-memcache-php7 \
 && phpize \
 && ./configure --enable-memcache \
 && make \
 && cp modules/memcache.so /usr/local/lib/php/extensions/no-debug-non-zts-20190902 \
 && echo 'extension=memcache.so' > /usr/local/etc/php/conf.d/docker-php-ext-manual-memcache.ini

# PHP configuration
COPY config/php.ini /usr/local/etc/php/

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
