FROM php:7.2-fpm

# common
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates wget \
        curl \
        git \
        ntp \
        openssh-client \
        # for intl extension
        libicu-dev \
        libz-dev \
        libpq-dev \
        libjpeg-dev \
        libpng-dev \
        libfreetype6-dev \
        libssl-dev \
        libxslt-dev \
        # for amp lib
        librabbitmq-dev \
        # for mcrypt extension
        libmcrypt-dev \
        libmagickwand-dev \
        libssh2-1 \
        libssh2-1-dev

RUN rm -r /var/lib/apt/lists/*

# Install the PHP extention
RUN docker-php-ext-install bcmath intl pdo_mysql \
    && docker-php-ext-configure bcmath --enable-bcmath \
    && docker-php-ext-configure intl --enable-intl \
    && docker-php-ext-install gd \
    && docker-php-ext-configure gd \
        --enable-gd-native-ttf \
        --with-jpeg-dir=/usr/lib \
        --with-freetype-dir=/usr/include/freetype2 \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install opcache \
    && docker-php-ext-install soap \
    && docker-php-ext-install exif \
    && docker-php-ext-install xsl \
    && docker-php-ext-install zip \
    && docker-php-ext-install pcntl \
    && docker-php-ext-enable pcntl \
    && pecl install imagick-beta \
    && docker-php-ext-enable imagick \
    && pecl install ssh2-1.1.2 \
    && docker-php-ext-enable ssh2 \
    && php -r "readfile('https://getcomposer.org/installer');" | php -- --install-dir=/usr/local/bin --filename=composer \
    && chmod +x /usr/local/bin/composer

# driver mongodb
RUN pecl install mongodb
RUN echo "extension=mongodb.so" >  $PHP_INI_DIR/conf.d/mongodb.ini

### Ampq lib
RUN pecl install amqp

# ext-sockets
RUN docker-php-ext-install sockets

# Time Zone
RUN echo "Europe/Paris" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

# Conf php
COPY php.ini $PHP_INI_DIR/conf.d/php.ini