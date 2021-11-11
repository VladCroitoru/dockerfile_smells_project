FROM php:7.1-cli
MAINTAINER Jonathan Garbee <jonathan@garbee.me>
# Install modules
RUN apt-get update -yqq && apt-get install -yqq \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmagickwand-dev \
        libpng12-dev \
        libpq-dev \
        libbz2-dev \
        postgresql-client-9.4 \
        libsqlite3-dev \
        libicu-dev \
        unzip \
        curl \
        git \
        libcurl3-dev \
        libxml2-dev \
    && pecl install imagick \
    && docker-php-ext-enable imagick \
    && docker-php-ext-configure intl \
    && docker-php-ext-install curl iconv pdo_pgsql zip bcmath mbstring intl xml soap \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd
CMD ["php", "-a"]

