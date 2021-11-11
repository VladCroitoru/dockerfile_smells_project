FROM php:7-alpine
MAINTAINER Wodby <admin@wodby.com>

RUN apk add --no-cache bash curl

COPY composer.json ./

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    composer global require hirak/prestissimo:^0.3 && \
    composer install --no-interaction --optimize-autoloader

COPY cleanup.php ./

ENTRYPOINT ["php", "cleanup.php"]
