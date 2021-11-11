FROM php:5.6-fpm
COPY php.ini /usr/local/etc/php/
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    libssl-dev \
    libc-client-dev \
    libkrb5-dev \
    libgmp-dev \
    re2c \
    libmhash-dev \
    php5-mysql \
    cron \
&& docker-php-ext-install iconv mcrypt \
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
&& docker-php-ext-install gd \
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
&& docker-php-ext-install imap \
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/local/include/ \
&& docker-php-ext-install gmp \
&& docker-php-ext-install mysql
