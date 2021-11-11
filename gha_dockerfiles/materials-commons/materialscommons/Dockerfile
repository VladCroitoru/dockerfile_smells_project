FROM php:7.3-cli
RUN apt-get update -y && apt-get install -y openssl zip unzip git libpng-dev zlib1g-dev libzip-dev
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN docker-php-ext-install pdo mbstring bcmath gd zip exif
WORKDIR /app
COPY . /app
RUN composer install
CMD php artisan serve --host=0.0.0.0 --port=8181
EXPOSE 8181
