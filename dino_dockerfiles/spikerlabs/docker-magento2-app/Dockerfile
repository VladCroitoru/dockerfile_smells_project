FROM php:7.0.13-fpm

RUN apt-get update && \
    apt-get install -y git libcurl4-gnutls-dev libpng3-dev libmagickwand-dev libmcrypt-dev libxslt1-dev libicu-dev && \
    docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install bcmath curl gd mcrypt pdo pdo_mysql simplexml soap xsl zip intl && \
    echo "\n" | pecl install imagick && \
    echo "extension=imagick.so" > /usr/local/etc/php/conf.d/docker-php-ext-imagick.ini && \
    curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /var/www

COPY ./scripts /root/scripts
