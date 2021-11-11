FROM php:7.1-fpm

RUN apt-get update

RUN apt-get install -y \
        git \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

# Some basic extensions
RUN docker-php-ext-install -j$(nproc) json mbstring opcache pdo pdo_mysql mysqli

# Intl
RUN apt-get install -y libicu-dev
RUN docker-php-ext-install -j$(nproc) intl

# Install bcmath
RUN docker-php-ext-install bcmath

# Install Memcached
RUN apt-get install -y libmemcached-dev zlib1g-dev
RUN pecl install memcached
RUN docker-php-ext-enable memcached

# Install APCu and APC backward compatibility
RUN pecl install apcu \
    && pecl install apcu_bc-1.0.3 \
    && docker-php-ext-enable apcu --ini-name 10-docker-php-ext-apcu.ini \
    && docker-php-ext-enable apc --ini-name 20-docker-php-ext-apc.ini

# Install mongo
RUN apt-get update && apt-get install -y \
        libssl-dev \
    && pecl install mongodb \
    && docker-php-ext-enable mongodb

# Install ldap
RUN apt-get install libldap2-dev -y && \
    docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \
    docker-php-ext-install ldap

# Install zip
RUN apt-get install -y zlib1g-dev && docker-php-ext-install zip

RUN docker-php-ext-install exif

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN apt-get clean && apt-get autoclean && apt-get autoremove -y
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install imagick
RUN apt-get update && apt-get install -y libmagickwand-dev --no-install-recommends \
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config /usr/bin \
&& pecl install imagick \
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini

ADD php.ini /usr/local/etc/php/conf.d/
ADD www.conf /usr/local/etc/php-fpm.d/

RUN chown -R www-data:www-data /var/www

WORKDIR /var/www/html

CMD ["php-fpm"]

EXPOSE 9000