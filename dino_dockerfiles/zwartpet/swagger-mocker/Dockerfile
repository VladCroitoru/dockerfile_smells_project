FROM php:7-apache

RUN apt-get update \
        && apt-get install -y libicu-dev git vim tar curl \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

RUN curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer

RUN docker-php-ext-install opcache intl && a2enmod rewrite && mkdir /var/www/html/web
RUN sed -i 's/\/var\/www\/html/\/var\/www\/html\/web/g' /etc/apache2/sites-available/000-default.conf

COPY . /var/www/html
RUN make -e install
RUN chown -R www-data:www-data /var/www/html