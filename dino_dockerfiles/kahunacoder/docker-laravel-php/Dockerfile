FROM php:7.0-fpm

MAINTAINER "Gary Smith" <docker@kc.gs>

RUN apt-get update && apt-get install -y \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
		libcurl4-gnutls-dev \
		libxml2-dev \
		libbz2-dev \
		re2c \
		libpng++-dev \
        libpng3 \
        libjpeg-dev \
        libvpx-dev \
        zlib1g-dev \
        libgd-dev \
        libssl-dev \
        libtidy-dev \
        libxslt1-dev \
        libmagic-dev \
        libexif-dev \
        file \
        libssh2-1-dev \
        git \
        wget	\    
		sqlite3	\
		libsqlite3-dev \


	&& docker-php-ext-install json \
	&& docker-php-ext-install mbstring \
	&& docker-php-ext-install tokenizer \
    && docker-php-ext-install gd \
	&& docker-php-ext-install curl \
	&& docker-php-ext-install dom \
	&& docker-php-ext-install bz2 \
	&& docker-php-ext-install mysqli \
	&& docker-php-ext-install pcntl \
	&& docker-php-ext-install pdo \
	&& docker-php-ext-install pdo_mysql \
	&& docker-php-ext-install phar \
	&& docker-php-ext-install posix \
	&& docker-php-ext-install simplexml \
	&& docker-php-ext-install soap \
	&& docker-php-ext-install sockets \
	&& docker-php-ext-install tidy \
	&& docker-php-ext-install zip \
	&& docker-php-ext-install bcmath \
	&& docker-php-ext-install calendar \
	&& docker-php-ext-install ctype \
	&& docker-php-ext-install exif \
	&& docker-php-ext-install pcntl \
	&& docker-php-ext-install pdo_sqlite


