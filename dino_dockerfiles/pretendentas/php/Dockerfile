FROM php:5.6-fpm
LABEL maintainer "karolis@pretendentas.lt"

RUN set -ex \
    && apt-get update && apt-get install -y \
        cron \
        git \
        libbz2-dev \
        libgmp-dev \
        libjpeg-dev \
        libmcrypt-dev \
        libpng12-dev \
        libxml2-dev \
        libxslt-dev \
        libtidy-dev \
        zip \
    && rm -rf /var/lib/apt/lists/*

RUN set -ex \
    && ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \
    && docker-php-ext-configure gd --with-png-dir=/usr/ --with-jpeg-dir=/usr/ \
    && docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \
    && docker-php-ext-configure mysql --with-mysql=mysqlnd \
    && docker-php-ext-configure mysqli --with-mysqli=mysqlnd
    
RUN set -ex \
    && docker-php-ext-install -j$(nproc) \
        bcmath \
        bz2 \
        calendar \
        exif \
        gd \
        gettext \
        gmp \
        mcrypt \
        mysql \
        mysqli \
        opcache \
        pcntl \
        pdo_mysql \
        shmop \
        soap \
        sockets \
        sysvmsg \
        sysvsem \
        sysvshm \
        tidy \
        wddx \
        xsl \
        zip

RUN set -ex \
    && mkdir -p /var/lib/php/session \
    && mkdir -p /var/lib/php/wsdlcache \
    && chown -R www-data:www-data /var/lib/php/session \
    && chown -R www-data:www-data /var/lib/php/wsdlcache

ENV GITHUB_TOKEN 87dc62834bd4267a86c4602b4efd381cfb6c8f14

RUN set -ex \
    && curl -sS https://getcomposer.org/installer | php -- \
        --install-dir=/usr/bin \
        --filename=composer \
    && composer config -g github-oauth.github.com $GITHUB_TOKEN


VOLUME /var/www/html
WORKDIR /var/www/html
EXPOSE 9000

COPY init.sh /init.sh
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["php-fpm"]