FROM php:7.0-apache

RUN apt-get update; apt-get install -y unzip
RUN docker-php-ext-install mysqli
COPY srdb.class.php /var/www/html
COPY srdb.cli.php /var/www/html
COPY index.php /var/www/html
