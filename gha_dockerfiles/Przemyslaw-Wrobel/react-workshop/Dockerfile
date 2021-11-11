FROM php:8.0-cli

RUN apt-get update && apt-get install -y
RUN docker-php-ext-install pdo pdo_mysql

RUN mkdir /app

WORKDIR /app

COPY ./ ./

ENTRYPOINT ["php"]
