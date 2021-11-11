FROM composer:1.3.2

MAINTAINER Kosta Harlan <kosta@savaslabs.com>

COPY . /app

RUN composer install -n --prefer-dist

ENTRYPOINT ["php", "siros.php"]