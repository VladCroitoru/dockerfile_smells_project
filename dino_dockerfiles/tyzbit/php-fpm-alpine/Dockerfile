FROM php:fpm-alpine

RUN sed -i 's/\[::\]/0.0.0.0/g' /usr/local/etc/php-fpm.d/zz-docker.conf

WORKDIR /var/www/html
EXPOSE 9000
CMD ["php-fpm"]
