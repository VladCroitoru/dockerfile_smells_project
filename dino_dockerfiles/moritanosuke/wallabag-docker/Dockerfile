FROM php:7.2-apache-buster
MAINTAINER carsten@kopis.de

ENV WALLABAG_VERSION=2.1.5 \
    SYMFONY_ENV=prod

# install PHP extensions and other dependencies
RUN apt-get update && apt-get install -y \
        git \
        zip unzip \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        && docker-php-ext-install -j$(nproc) iconv \
        && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
        && docker-php-ext-install -j$(nproc) gd \
        && docker-php-ext-install bcmath \
        && pecl install mcrypt \
        && docker-php-ext-enable mcrypt
# install composer
RUN cd /usr/local/bin && curl -s http://getcomposer.org/installer | php
# download wallabag
RUN curl -o wallabag.tar.gz -L https://github.com/wallabag/wallabag/archive/${WALLABAG_VERSION}.tar.gz && \
    tar xvzf wallabag.tar.gz && \
    mv wallabag-${WALLABAG_VERSION} /var/www/wallabag && \
    rm wallabag.tar.gz
# install via composer
RUN cd /var/www/wallabag && \
    /usr/local/bin/composer.phar install --no-dev -o --prefer-dist && \
    php bin/console wallabag:install --env=prod && \
    chown -R www-data:www-data /var/www/wallabag && \
    rmdir /var/www/html && \
    ln -s /var/www/wallabag/web /var/www/html
