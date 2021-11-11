FROM php:7-fpm

RUN apt-get update \
    && apt-get -y install \
            libmagickwand-dev \
			libmcrypt-dev \
			libpng12-dev \
            libjpeg62-turbo-dev \
            libfreetype6-dev \
            libmemcached-dev \
            libicu-dev \
			--no-install-recommends \
    && pecl install imagick \
    && docker-php-ext-enable imagick \
    && curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-dev/php-memcached/archive/php7.tar.gz" \
    && mkdir -p /usr/src/php/ext/memcached \
    && tar -C /usr/src/php/ext/memcached -zxvf /tmp/memcached.tar.gz --strip 1 \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-configure memcached \
    && docker-php-ext-install gd mcrypt mysqli pdo_mysql zip calendar opcache memcached exif intl sockets

# Clean repository
RUN apt-get clean \
	&& rm -rf /tmp/* /var/cache/apk/* /var/lib/apt/lists/* \