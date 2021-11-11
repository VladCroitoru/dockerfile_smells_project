FROM php:8.0.3-apache
COPY . /var/www/html
COPY --from=composer /usr/bin/composer /usr/bin/composer
RUN apt-get update && apt-get install -y git zip unzip
RUN composer install --prefer-dist --no-progress
# RUN pecl install xdebug && docker-php-ext-enable xdebug
RUN apt-get install -y libpq-dev \
    && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
    && docker-php-ext-install pdo pdo_pgsql pgsql
COPY .docker/000-default.conf /etc/apache2/sites-enabled/
RUN a2enmod rewrite
RUN composer update