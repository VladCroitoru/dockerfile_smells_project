FROM php:apache

MAINTAINER Thiago Moreira <loganguns@gmail.com>

COPY ./config/apache/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY ./config/php/php.ini /usr/local/etc/php/

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        imagemagick \
        openssh-client \
        sudo \
        git \
        libmemcached-dev \
        libssl-dev \
        libpng12-dev \
        libjpeg-dev \
        re2c \
        libfreetype6-dev \
        libmcrypt-dev \
        libxml2-dev && \
    rm -r /var/lib/apt/lists/*


RUN cd /tmp/ && \
    git clone https://github.com/php-memcached-dev/php-memcached.git /usr/src/php/ext/memcached && \
    cd /usr/src/php/ext/memcached && \
    git checkout php7 && \
    pecl install mongodb \
    && echo "extension=mongodb.so" > $PHP_INI_DIR/conf.d/mongodb.ini

RUN docker-php-ext-configure gd --with-jpeg-dir --with-png-dir --with-freetype-dir && \
	docker-php-ext-install gd && \
	docker-php-ext-install mcrypt && \
	docker-php-ext-install mbstring && \
	docker-php-ext-install bcmath && \
	docker-php-ext-install opcache && \
	docker-php-ext-install memcached && \
	docker-php-ext-install pdo pdo_mysql && \
	docker-php-ext-install mysqli && \
        a2ensite 000-default.conf && \
	a2enmod rewrite

WORKDIR /var/app/web
