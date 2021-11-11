FROM php:7.0-fpm-alpine

RUN apk add  --update --no-cache curl-dev libcurl libpng-dev
RUN docker-php-ext-install ctype gd iconv pdo pdo_mysql mysqli

RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*

ADD app.ini /usr/local/etc/php/conf.d/

ADD app.pool.conf /usr/local/etc/php-fpm.d/

CMD ["php-fpm"]

EXPOSE 9000
EXPOSE 9001
