FROM php:7.3-fpm

ENV STAGING_ENV prod

ENV USER_UID 1000
ENV USER_GID 1000
ENV SSH_AUTH_SOCK /ssh-agent
ENV SSH_PRIVATE_KEY /home/www-data/private_key

RUN mkdir -p /home/www-data
RUN mkdir -p /var/www/html

# common
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates wget \
        curl \
        git \
        ntp \
        nano \
        openssh-client \
        # for intl extension
        libicu-dev \
        libz-dev \
        libpq-dev \
        libjpeg-dev \
        #libpng12-dev \
        libfreetype6-dev \
        libssl-dev \
        libxslt-dev \
        # for mcrypt extension
        libmcrypt-dev \
        libmagickwand-dev \
        supervisor \
        subversion make g++ python chrpath \
        && rm -r /var/lib/apt/lists/* && \
        sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf

VOLUME ["/etc/supervisor/conf.d"]
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

RUN cd /tmp && wget http://curl.haxx.se/ca/cacert.pem && mv /tmp/cacert.pem /usr/lib/ssl/cert.pem

# Install the PHP extention
RUN docker-php-ext-install mcrypt bcmath intl pdo_mysql \
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
    && docker-php-ext-install pcntl \
    && docker-php-ext-install zip \
    && pecl install imagick-beta \
    && docker-php-ext-enable imagick \
    && php -r "readfile('https://getcomposer.org/installer');" | php -- --install-dir=/usr/local/bin --filename=composer \
    && chmod +x /usr/local/bin/composer

RUN pecl install mongodb
RUN echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/mongodb.ini

###xdebug
ENV XDEBUG_VERSION 2.6.1
RUN pecl install channel://pecl.php.net/xdebug-${XDEBUG_VERSION}

RUN usermod -u 1000 www-data

# Time Zone
RUN echo "Europe/Paris" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" > $PHP_INI_DIR/conf.d/date_timezone.ini

# Memory Limit
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini

#entry point
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set up the command arguments.
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["php-fpm"]
