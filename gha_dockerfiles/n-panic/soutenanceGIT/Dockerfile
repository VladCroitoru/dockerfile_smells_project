FROM docker.io/library/php:5.6-apache

USER root

WORKDIR /var/www/html

# Update & install
RUN apt-get update && apt-get install -y \
        zlib1g-dev \
        libzip-dev \
        zip \
        curl \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install zip \
    && docker-php-source delete

# APACHE CONFIGURATION
ENV APACHE_DOCUMENT_ROOT=/var/www/html/public
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

RUN a2enmod rewrite headers

# PHP.INI to set the timezone
RUN cp "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"
RUN sed -ri -e 's!;date.timezone =!date.timezone = "Europe/Paris"!g' $PHP_INI_DIR/php.ini

# XDebug
# RUN pecl install xdebug && docker-php-ext-enable xdebug
# COPY ./xdebug.ini /usr/local/etc/conf.d/xdebug.ini

# Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

RUN chown -R www-data:www-data /var/www/html \
    && a2enmod rewrite

# CMD bash -c "php -S localhost:8000 -t public/"
CMD php artisan migrate:refresh --seed && apache2-foreground