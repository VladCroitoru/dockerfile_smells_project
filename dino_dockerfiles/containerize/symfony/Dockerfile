FROM php:7.0-fpm

# extension - except: imagick apc xdebug geoip redis
RUN apt-get update && apt-get install -y git openssh-client \
    libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev \
    zlib1g-dev libicu-dev g++ \
    libxslt-dev \
    libbz2-dev \
    --no-install-recommends && rm -r /var/lib/apt/lists/*

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ 
RUN docker-php-ext-configure intl
RUN docker-php-ext-install opcache iconv mcrypt mysqli pdo pdo_mysql mbstring gd bcmath calendar exif intl sockets xsl zip bz2

# extension - redis
RUN pecl install -o -f redis \
    && rm -rf /tmp/pear \
    && echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini

# composer
ENV COMPOSER_HOME /composer

# Allow Composer to be run as root
ENV COMPOSER_ALLOW_SUPERUSER 1

RUN curl -sS https://getcomposer.org/installer | php -- \
    --install-dir=/usr/local/bin \
    --filename=composer

RUN usermod -u 1000 www-data

WORKDIR /symfony

EXPOSE 9000

VOLUME ["/user/local/etc/php/conf.d/symfony.ini"]
VOLUME ["/etc/php-fpm.conf"]

CMD ["php-fpm", "-F"]