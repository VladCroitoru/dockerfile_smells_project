FROM php:7-alpine

RUN apk add --no-cache libmcrypt-dev freetype-dev libpng-dev libjpeg-turbo-dev freetype libpng libjpeg-turbo \
    && docker-php-ext-configure gd --with-gd --with-freetype-dir=/usr/include/ --with-png-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install bcmath gd mbstring mcrypt mysqli pdo pdo_mysql opcache tokenizer zip \
    && apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev
    
WORKDIR /var/www

ENTRYPOINT ["php", "artisan"]

CMD ["--help"]
