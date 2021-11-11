ARG BASE_IMAGE
FROM $BASE_IMAGE

ADD apache2.conf /etc/apache2/apache2.conf
ADD 000-default.conf /etc/apache2/sites-available/000-default.conf
ADD symfony.ini /usr/local/etc/php/conf.d/symfony.ini
ADD mpm_prefork.conf /etc/apache2/mods-available/mpm_prefork.conf
RUN rm /etc/apache2/conf-available/security.conf && rm /etc/apache2/conf-enabled/security.conf

RUN apt-get update \
    && apt-get install -y libicu-dev git wget unzip libpng-dev libjpeg62-turbo-dev libzip-dev libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN ( \
       docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ \
       || docker-php-ext-configure gd --with-jpeg \
    ) \
    && docker-php-ext-install pdo_mysql pdo_pgsql pgsql opcache intl zip gd \
    && a2enmod rewrite headers

RUN pecl install apcu \
    && pecl clear-cache \
    && echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini


# Upload settings
RUN echo "file_uploads = On\n" \
         "memory_limit = 256M\n" \
         "upload_max_filesize = 256M\n" \
         "post_max_size = 256M\n" \
         "max_execution_time = 30\n" \
         > /usr/local/etc/php/conf.d/uploads.ini

# General PHP settings
RUN echo "display_errors = 0\n" \
         "display_startup_errors = 0" \
         > /usr/local/etc/php/conf.d/general.ini

# https://getcomposer.org/doc/03-cli.md#composer-allow-superuser
ENV COMPOSER_ALLOW_SUPERUSER 1

# Install composer
RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && mkdir /var/www/html/public

ARG NODE_VERSION
RUN curl -SLO "https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-x64.tar.xz" \
    && tar -xJf "node-$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
    && rm "node-$NODE_VERSION-linux-x64.tar.xz" \
    && ln -s /usr/local/bin/node /usr/local/bin/nodejs \
    && npm install --global yarn

ARG LIBVIPS_VERSION=8.8.3
ARG ENABLE_IMAGE_SUPPORT=false
RUN $ENABLE_IMAGE_SUPPORT \
 && apt-get update \
 && apt-get install -y --no-install-recommends build-essential pkg-config libglib2.0-dev libexpat1-dev \
 # Image format packages JPEG, EXIF, GIF, Quantized PNG, Text rendering, WebP
 libjpeg62-turbo-dev libexif-dev libgif-dev libpango1.0-dev libwebp-dev libmagickwand-dev \
 && cd /tmp \
 && curl -L -O https://github.com/libvips/libvips/releases/download/v$LIBVIPS_VERSION/vips-$LIBVIPS_VERSION.tar.gz \
 && tar zxvf vips-$LIBVIPS_VERSION.tar.gz \
 && cd /tmp/vips-$LIBVIPS_VERSION \
 && ./configure \
 && make \
 && make install \
 && ldconfig \
 && apt-get remove -y build-essential \
 && apt-get autoremove -y \
 && apt-get autoclean \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 && pecl install vips imagick \
 && docker-php-ext-enable vips imagick \
 || true

ARG ENABLE_DEBUG=false
RUN $ENABLE_DEBUG \
 && pecl install -f xdebug \
 && pecl clear-cache && rm -rf /tmp/pear \
 && echo "zend_extension=$(ls /usr/local/lib/php/*/*/xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
 && echo "xdebug.remote_enable = On" >> /usr/local/etc/php/conf.d/xdebug.ini \
 && echo "xdebug.remote_autostart = On" >> /usr/local/etc/php/conf.d/xdebug.ini \
 && echo "xdebug.remote_connect_back = On" >> /usr/local/etc/php/conf.d/xdebug.ini \
 && echo "xdebug.coverage_enable = Off" >> /usr/local/etc/php/conf.d/xdebug.ini \
 && sed -i.bak "s/opcache.validate_timestamps=0/opcache.validate_timestamps=1/g" /usr/local/etc/php/conf.d/symfony.ini \
 && sed -i.bak "s/display_errors = 0/display_errors = 1/g" /usr/local/etc/php/conf.d/general.ini \
 && sed -i.bak "s/display_startup_errors = 0/display_startup_errors = 1/g" /usr/local/etc/php/conf.d/general.ini \
 || true
