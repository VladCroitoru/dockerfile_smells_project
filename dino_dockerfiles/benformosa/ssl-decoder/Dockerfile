FROM php:7-apache

ADD docker/testing.list /etc/apt/sources.list.d/testing.list

RUN apt-get update \
    && apt-get install -y --no-install-recommends -t stable \
	openssl/testing \
        dnsutils \
        g++ \
        libfreetype6-dev \
        libicu-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        perl \
        python-all-dev \
        python-netaddr \   
        python2.7 \
        zlib1g-dev
    
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin \
    && docker-php-ext-configure intl \
    && docker-php-ext-install -j$(nproc) iconv \
    && docker-php-ext-install -j$(nproc) mcrypt \
    && docker-php-ext-install -j$(nproc) mbstring \
    && docker-php-ext-install -j$(nproc) bcmath \
    && docker-php-ext-install -j$(nproc) intl \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

ADD . /var/www/html
