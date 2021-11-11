FROM php:apache
# Install modules
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
	libxml2-dev \
    && a2enmod rewrite \
    && docker-php-ext-install iconv \
    && docker-php-ext-install mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install soap \
    && docker-php-ext-install opcache \
    && rm -rf /var/lib/apt/lists/*

COPY php.ini /usr/local/etc/php/
