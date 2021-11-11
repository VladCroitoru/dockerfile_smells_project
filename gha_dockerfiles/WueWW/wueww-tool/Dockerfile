FROM php:7.3-cli AS builder

# install composer to /composer.phar
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
    git \
    unzip \
    yarnpkg

# copy app sources
COPY / /app
WORKDIR /app

RUN php /composer.phar install

RUN yarnpkg install
RUN yarnpkg build

#------------------------------------------------------------------------------

FROM php:7.3-apache

ENV APACHE_DOCUMENT_ROOT /app/public

RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf && \
    sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf && \
    sed -ri -e 's!Options Indexes FollowSymLinks!FallbackResource /index.php!' /etc/apache2/apache2.conf

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini" && \
    echo 'date.timezone = "Europe/Berlin"' > $PHP_INI_DIR/conf.d/timezone.ini && \
    echo 'variables_order = "GPCSE"' > $PHP_INI_DIR/conf.d/variables-order.ini

COPY --from=builder /app /app
WORKDIR /app

RUN bin/console doctrine:database:create -n && \
    bin/console doctrine:schema:create -n && \
    bin/console doctrine:fixtures:load -n

ENV APP_ENV=prod
RUN bin/console cache:warmup -n && \
    chown -R www-data. var/ public/logos/
