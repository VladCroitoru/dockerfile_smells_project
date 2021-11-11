FROM php:7.0-apache

MAINTAINER Stefan Kreuter <kreuter@gigatec.de>

RUN usermod -u 500 www-data && groupmod -g 500 www-data

RUN a2enmod rewrite && a2enmod expires && a2enmod headers

RUN rm -rf /var/www/html/*

RUN requirements="libpng12-dev libmcrypt-dev libmcrypt4 libcurl3-dev libfreetype6 libjpeg62-turbo libjpeg62-turbo-dev libpng12-dev libfreetype6-dev libicu-dev libxslt1-dev vim git wget colordiff curl rsync ssh mysql-client zip ssmtp cron" \
    && apt-get update && apt-get install -y $requirements && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install mcrypt \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install zip \
    && docker-php-ext-install intl \
    && docker-php-ext-install xsl \
    && docker-php-ext-install soap \
    && docker-php-ext-install mysqli \
    && requirementsToRemove="libpng12-dev libmcrypt-dev libcurl3-dev libpng12-dev libfreetype6-dev libjpeg62-turbo-dev" \
    && apt-get purge --auto-remove -y $requirementsToRemove

COPY ./etc/* /usr/local/etc/php/conf.d/

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /var/www/html
VOLUME /var/www/html
