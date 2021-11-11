FROM php:7.2-alpine
 
RUN apk add --no-cache git freetype-dev libpng-dev libjpeg-turbo-dev freetype libpng libjpeg-turbo \
    && docker-php-ext-configure gd --with-gd --with-freetype-dir=/usr/include/ --with-png-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install bcmath gd mbstring mysqli pdo pdo_mysql opcache tokenizer zip \
    && apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer 

WORKDIR /var/www

RUN composer self-update

ENTRYPOINT ["composer"]

CMD ["--help"]
