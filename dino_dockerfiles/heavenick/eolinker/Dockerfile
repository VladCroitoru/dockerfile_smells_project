FROM php:7-apache


RUN docker-php-ext-install mbstring mysqli pdo pdo_mysql shmop
 
COPY ./ /var/www/html/

RUN chmod -R 777 /var/www/html/ 

