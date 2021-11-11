FROM php:5-fpm-alpine

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/bin/composer

RUN mkdir -p /run/nginx

RUN apk add --update vim postgresql-dev freetype-dev libmcrypt-dev libjpeg-turbo-dev libpng-dev zlib-dev nginx

RUN docker-php-ext-install iconv mcrypt pdo pdo_pgsql pdo_mysql opcache zip mysql

COPY ./artifacts/default /etc/nginx/conf.d/default.conf
COPY ./artifacts/nginx /etc/nginx/nginx.conf

RUN mkdir /logs
RUN echo "php_admin_value[display_errors] = On">>/usr/local/etc/php-fpm.d/www.conf
RUN echo "php_admin_value[error_reporting] = E_ALL & ~E_DEPRECATED">>/usr/local/etc/php-fpm.d/www.conf

EXPOSE 80

ENTRYPOINT nginx && php-fpm -F
