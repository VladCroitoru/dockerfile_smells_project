FROM php:5.6-fpm

RUN apt-get update -y \
    && apt-get install -y libmemcached-dev \
        libtidy-dev \
        libxml2-dev \
        libxslt1-dev \
        libzip-dev \
        zlib1g-dev \
        libpspell-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd iconv mcrypt exif fileinfo mysqli pdo_mysql pcntl tidy xmlrpc xsl zip bcmath pspell shmop sockets \
    && sh -c 'printf "\n" | pecl install memcached' \
    && docker-php-ext-enable memcached opcache \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
