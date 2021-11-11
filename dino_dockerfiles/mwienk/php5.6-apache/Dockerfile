FROM php:5.6-apache
MAINTAINER Mark Wienk <mark@wienkit.nl>

RUN requirements="libpng12-dev libjpeg-dev libjpeg62-turbo libmcrypt4 libmcrypt-dev libcurl3-dev libxml2-dev libxslt-dev libicu-dev libicu52" \
    && apt-get update && apt-get install -y $requirements && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-configure gd --with-jpeg-dir=/usr/lib \
    && docker-php-ext-install gd \
    && docker-php-ext-install mcrypt \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install soap \
    && docker-php-ext-install xsl \
    && docker-php-ext-install intl \
    && requirementsToRemove="libpng12-dev libjpeg-dev libmcrypt-dev libcurl3-dev libxml2-dev libicu-dev" \
    && apt-get purge --auto-remove -y $requirementsToRemove \
    && echo "always_populate_raw_post_data=-1" > /usr/local/etc/php/php.ini

RUN curl -sSL https://getcomposer.org/composer.phar -o /usr/bin/composer \
    && chmod +x /usr/bin/composer \
    && apt-get update && apt-get install -y zlib1g-dev git && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install zip \
    && apt-get purge -y --auto-remove zlib1g-dev \
    && composer selfupdate

RUN sed -i "s/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www/" /etc/apache2/apache2.conf \
    && rm -rf /var/www && mkdir -p /var/www

VOLUME ["/var/www"]

WORKDIR /var/www

RUN usermod -u 1000 www-data
RUN chown -R www-data:www-data /var/www
RUN a2enmod rewrite

RUN apt-get update \
    && apt-get install -y libxslt-dev \
    && docker-php-ext-install xsl
