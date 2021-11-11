FROM php:7.1-fpm

RUN apt-get update && apt-get install -y openssh-client zip unzip libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng-dev libpq-dev libicu-dev libxslt1.1 libxslt1-dev libssl-dev libcurl4-openssl-dev pkg-config; exit 0

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer; exit 0

RUN docker-php-ext-install iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
    && docker-php-ext-install pdo pdo_pgsql pgsql \
    && docker-php-ext-install opcache pdo pdo_pgsql pgsql sockets intl; exit 0
