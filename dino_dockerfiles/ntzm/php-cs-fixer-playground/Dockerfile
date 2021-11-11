FROM node:10 as build-assets

COPY package* ./

RUN npm ci

COPY gulpfile.js .
COPY assets assets

RUN node_modules/.bin/gulp

FROM php:7.3-apache

WORKDIR /var/www/

ENV PORT 80

EXPOSE $PORT

RUN apt-get update \
 && apt-get install -y \
    libpq-dev \
    unzip \
 && docker-php-ext-install \
    opcache \
    pdo_pgsql \
 && a2enmod rewrite \
 && php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer

COPY composer.* ./

RUN composer install --optimize-autoloader --prefer-dist --no-dev

COPY --from=build-assets html/app.js html
COPY --from=build-assets html/style.css html

COPY . .

RUN chown -R www-data:www-data .

CMD sed -i "s/80/$PORT/g" /etc/apache2/sites-available/000-default.conf /etc/apache2/ports.conf \
 && docker-php-entrypoint apache2-foreground
