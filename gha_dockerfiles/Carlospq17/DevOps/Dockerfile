FROM php:7.4-fpm-alpine
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN docker-php-ext-install pdo pdo_mysql
WORKDIR /app
COPY . /app
RUN composer update
RUN composer install

RUN php artisan mysql:createdb 
RUN php artisan migrate:fresh 
RUN php artisan db:seed 

CMD php artisan serve --host=0.0.0.0 --port=8000

EXPOSE 8000