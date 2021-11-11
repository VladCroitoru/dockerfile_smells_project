FROM php:7.0.33-fpm-alpine
RUN apk upgrade --update && apk add \
    coreutils \
    autoconf \
    build-base \
    pcre-dev \
    gcc \
    g++ \
    make \
    automake \
    file \
    libtool \
    freetype-dev \
    libjpeg-turbo-dev \
    libltdl \
    libmcrypt-dev \
    libpng-dev \
    gettext-dev \
    openssl \
    libintl \
    icu-dev \
    openldap-dev \
    freetype \
    libjpeg-turbo-dev \
    libpng-dev \
    ttf-dejavu \
    mysql-client \
    pkgconfig \
    libxml2-dev \
    libxml2 \
    git \
    icu-libs \
    unzip \
    curl \
    curl-dev \
    libcurl \
    libexif-dev \
    postgresql-dev \
    imagemagick-dev \
    libmemcached-dev \
    re2c \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \
    --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd opcache iconv mcrypt pdo_pgsql \
    pdo_mysql mbstring mysqli soap intl zip curl exif bcmath \
    && pecl install imagick \
    && docker-php-ext-enable imagick

RUN cd /tmp && git clone git://github.com/alanxz/rabbitmq-c.git \
    && cd rabbitmq-c \
    && git submodule init \
    && git submodule update \
    && autoreconf -i \
    && ./configure --prefix=/usr/local/ \
    && make -j$(nproc) \
    && make install

RUN pecl install redis \
    && cd /tmp \
    && wget https://pecl.php.net/get/amqp-1.9.1.tgz \
    && tar -xvf amqp-1.9.1.tgz \
    && cd /tmp/amqp-1.9.1 \
    && phpize \
    && ./configure --with-librabbitmq-dir=/usr/local/ \
    && make -j$(nproc) \
    && make install \
    && docker-php-ext-enable redis amqp

RUN cd /tmp \
    && curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-dev/php-memcached/archive/php7.tar.gz" \
    && mkdir -p /tmp/memcached \
    && tar -C /tmp/memcached -zxvf /tmp/memcached.tar.gz --strip 1 \
    && ( \
        cd /tmp/memcached \
        && phpize \
        && ./configure  \
        && make -j$(nproc) \
        && make install \
    ) \
    && rm -r /tmp/memcached \
    && rm /tmp/memcached.tar.gz \
    && docker-php-ext-enable memcached

RUN rm -rf /var/cache/apk/*

COPY ./php.ini /usr/local/etc/php/conf.d/php.ini
COPY ./php-fpm.d/www.conf /usr/local/etc/php-fpm.d/www.conf

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php --install-dir=/bin --filename=composer

CMD ["php-fpm", "-F"]
