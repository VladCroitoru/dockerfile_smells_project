FROM php:7.4-fpm

WORKDIR /var/www
RUN rm -rf /var/www/html

COPY . /var/www
RUN chmod 777 -R /var/www/storage/logs/
RUN ln -s public html

EXPOSE 9000

