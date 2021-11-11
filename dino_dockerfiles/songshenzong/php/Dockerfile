# Use Alpine Linux
FROM php:7.3-fpm-alpine

# Maintainer
LABEL maintainer="Songshenzong <i@songshenzong.com>"

# Set Timezone Environments
ENV TIMEZONE            Asia/Shanghai

RUN apk add --update tzdata  \
	&& cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime  \
	&& echo "${TIMEZONE}" > /etc/timezone  \
	&& apk del tzdata  \
    && apk add --no-cache --virtual .build-deps \
                 curl \
                 g++ \
                 make \
                 autoconf \
                 openssl-dev  \
                 libaio  \
                 libaio-dev \
                 linux-headers \
                 zlib-dev \
    && apk add --no-cache \
                 bash \
                 openssh \
                 libssl1.0 \
                 libxslt-dev \
                 libjpeg-turbo-dev \
                 libwebp-dev \
                 libpng-dev \
                 libxml2-dev \
                 freetype-dev \
                 libmcrypt \
                 freetds-dev  \
                 libmemcached-dev  \
                 cyrus-sasl-dev  \
    && docker-php-source extract  \
    && docker-php-ext-configure pdo  \
    && docker-php-ext-configure pdo_mysql  \
    && docker-php-ext-configure mysqli  \
    && docker-php-ext-configure opcache  \
    && docker-php-ext-configure exif  \
    && docker-php-ext-configure sockets  \
    && docker-php-ext-configure soap  \
    && docker-php-ext-configure bcmath  \
    && docker-php-ext-configure pcntl  \
    && docker-php-ext-configure sysvsem  \
    && docker-php-ext-configure tokenizer  \
    && docker-php-ext-configure zip  \
    && docker-php-ext-configure xsl  \
    && docker-php-ext-configure shmop  \
    && docker-php-ext-configure gd \
                                --with-jpeg-dir=/usr/include \
                                --with-png-dir=/usr/include \
                                --with-webp-dir=/usr/include \
                                --with-freetype-dir=/usr/include  \
    && pecl install swoole redis xdebug mongodb memcached  \
    && pecl clear-cache  \
	&& docker-php-ext-enable swoole redis xdebug mongodb memcached \
    && docker-php-ext-install pdo \
                           pdo_mysql \
                           mysqli \
                           opcache \
                           exif \
                           sockets \
                           soap \
                           bcmath \
                           pcntl \
                           sysvsem \
                           tokenizer \
                           zip \
                           xsl \
                           shmop \
                           gd  \
    && docker-php-source delete  \
    && apk del .build-deps  \
    && ln -sf /dev/stdout /usr/local/var/log/php-fpm.access.log  \
    && ln -sf /dev/stderr /usr/local/var/log/php-fpm.error.log  \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer  \
    && curl --location --output /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar  \
    && chmod +x /usr/local/bin/phpunit

# Expose ports
EXPOSE 9000

# Entry point
CMD ["php-fpm"]
