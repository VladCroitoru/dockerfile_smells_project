FROM php:7.0-fpm
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        autoconf g++ make openssl libssl-dev libcurl4-openssl-dev \
        libcurl4-openssl-dev pkg-config \
	libsasl2-dev \
    && docker-php-ext-install -j$(nproc) iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN  pecl install yaf-3.0.6 && pecl install redis && pecl install mongodb-1.3.4

COPY php.ini /usr/local/etc/php/
COPY index.php /var/www/html/

