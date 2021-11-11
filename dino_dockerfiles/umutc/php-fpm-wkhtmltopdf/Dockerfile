FROM php:7.1.11-fpm

MAINTAINER Umut ÇELİK <mail@umutcelik.com.tr>

RUN apt-get update && apt-get install -y zlib1g-dev libicu-dev g++
RUN docker-php-ext-configure intl
RUN docker-php-ext-install intl

RUN apt-get update -y
RUN apt-get install -y libgmp-dev re2c libmhash-dev libmcrypt-dev file
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/local/include/
RUN docker-php-ext-configure gmp
RUN docker-php-ext-install gmp

RUN apt-get update && apt-get upgrade -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpq-dev \
    libmagickwand-dev \
    libpng12-dev \
    libmemcached-dev \
    libssl-dev \
    libssl-doc \
    libsasl2-dev \
    zlib1g-dev \
    libicu-dev \
    g++ \
    && docker-php-ext-install \
        bcmath \
        bz2 \
        calendar \
        dba \
        gettext \
        #ereg \
        #mhash \
        #mysql \
        iconv \
        mbstring \
        pcntl \
        shmop \
        exif \
        mysqli \
        pdo_mysql \
        opcache \
        soap \
        sockets \
        sysvmsg \
        sysvsem \
        sysvshm \
        wddx \
        zip \
    && docker-php-ext-configure gd \
        --with-freetype-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && pecl install redis && docker-php-ext-enable redis \
    && apt-get install -y \
        curl \
        libxrender1 \
        libfontconfig \
        libxtst6 \
        xz-utils \
    && curl "https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz" -L -o "wkhtmltopdf.tar.xz" \
    && tar Jxvf wkhtmltopdf.tar.xz \
    && mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf

RUN apt-get update && apt-get install -y zlib1g-dev libzmq-dev wget git \
    && pecl install zmq-beta \
    && docker-php-ext-install zip \
    && docker-php-ext-enable zmq
ADD install_composer.sh /install_composer.sh
RUN /install_composer.sh && rm /install_composer.sh
