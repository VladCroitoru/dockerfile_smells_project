FROM php:7-apache-jessie
#MAINTAINER porchn <pichai.chin@gmail.com>

ENV TZ=Asia/Bangkok
RUN echo $TZ > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
RUN mkdir -p /etc/apache2/ssl
RUN echo date.timezone = $TZ > /usr/local/etc/php/conf.d/docker-php-ext-timezone.ini

# Defaul config php.ini
COPY ./config/php.ini /usr/local/etc/php/
COPY ./index.php /var/www/html/
RUN echo 'ServerName localhost' >> /etc/apache2/apache2.conf

RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng-dev \
    libmagickwand-dev \
    libmemcached-dev \
    libssl-dev \
    libmcrypt-dev \
    libz-dev \
    libicu-dev \
    libcurl4-openssl-dev \
    libc-client-dev \
    libkrb5-dev \
    libpq-dev \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-configure imap --with-imap-ssl --with-kerberos \
    && docker-php-ext-install -j$(nproc) gd iconv mcrypt mysqli soap zip intl json mbstring imap curl
##  && docker-php-ext-install -j$(nproc) gd iconv mcrypt mysqli mysqlnd openssl odbc pdo_mysql soap zip zlib intl json mbstring

# Xdebug
RUN pecl install xdebug-2.5.0 \
    && docker-php-ext-enable xdebug

# Imagick
RUN pecl install imagick \
    && docker-php-ext-enable imagick

# Memcached
RUN pecl install memcached \
    && docker-php-ext-enable memcached

# install mongodb ext
RUN pecl install mongodb \
    && docker-php-ext-enable mongodb

# Clean apt cache
RUN rm -rf /var/lib/apt/lists/*

# Enable Apache mod_rewrite ssl
RUN a2enmod rewrite ssl headers
RUN usermod -u 1000 www-data
RUN chown -R www-data:www-data /var/www

# Create Volume
VOLUME [/etc/apache2/sites-enabled,/var/www,/var/log/apache2]

EXPOSE 80 443