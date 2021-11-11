FROM php:fpm
WORKDIR /app
COPY . .
RUN apt update -y \
&& apt install -y git unzip
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer
RUN composer i --no-dev
