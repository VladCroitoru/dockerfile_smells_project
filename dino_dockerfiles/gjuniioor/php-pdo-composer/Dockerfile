FROM php:7.2-cli-stretch

MAINTAINER Gildásio Júnior (gildasiojunior@infojr.com.br)

# update package list
RUN apt-get update

# install curl and git
RUN apt-get install -y curl git unzip

# install composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

# install pdo
RUN docker-php-ext-install pdo pdo_mysql

# install php gd
RUN apt install -y libpng-dev
RUN docker-php-ext-install gd

# install php mbstring and exif
RUN docker-php-ext-install exif mbstring

EXPOSE 8000

WORKDIR /var/www/html/

CMD ["php", "artisan", "serve", "--host", "0.0.0.0"]
