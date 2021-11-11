FROM php:8.0-apache
WORKDIR "/var/www/html/"
USER root
EXPOSE 80

RUN apt-get update && apt-get install -y curl ca-certificates git zip unzip libmemcached-dev zlib1g-dev libpng-dev libjpeg-dev libfreetype6-dev && apt-get clean \
    && pecl install memcached-3.1.5 \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-enable memcached \
    && docker-php-ext-configure gd --with-freetype=/usr/include/ --with-jpeg=/usr/include/ \
    && docker-php-ext-install pdo pdo_mysql \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-enable gd

# Config apache
COPY ./.docker/apache/vhost.conf /etc/apache2/sites-available/000-default.conf
RUN chown -R www-data:www-data /var/www/html && a2enmod rewrite

COPY . .

# Get latest Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer
RUN composer update && composer install
CMD php artisan migrate:fresh --seed && apache2-foreground