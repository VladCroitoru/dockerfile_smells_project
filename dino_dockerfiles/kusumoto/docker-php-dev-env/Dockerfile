FROM php:7.1-apache
# PHP 7.1.5
# Install modules
RUN apt-get update && apt-get install -y --force-yes \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        mysql-common \
        openssl \
        git \
        libpq-dev \
        libmemcached-dev \
        libicu-dev \
    && docker-php-ext-install iconv mcrypt mysqli mbstring intl calendar \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && pecl install xdebug \
    && echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20121212/xdebug.so" > /usr/local/etc/php/conf.d/ext-xdebug.ini

CMD ["apache2-foreground"]
