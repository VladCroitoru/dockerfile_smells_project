FROM php:7.4-fpm-alpine
RUN apk add git
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer
COPY ./app /var/www/html
RUN cd /var/www/html && \
    /usr/local/bin/composer install --no-dev

RUN chown -R www-data: /var/www/html