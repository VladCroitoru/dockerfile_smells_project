FROM php:7.0.9-apache
MAINTAINER Matt Oddie <docker@mattoddie.com>

RUN apt-get update && \
    apt-get install -y git

COPY config/php.ini /usr/local/etc/php/
COPY src/ /var/www/

# Install Composer and make it available in the PATH
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

WORKDIR /var/www/

# Install dependencies with Composer.
# --prefer-source fixes issues with download limits on Github.
# --no-interaction makes sure composer can run fully automated
RUN composer install --prefer-source --no-interaction
RUN chmod 777 /var/www/data/cache
