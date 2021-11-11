FROM php:7.4.24-apache-buster
LABEL Dare=dare@zooto.io

RUN apt-get update --fix-missing && apt-get install -y \
    default-mysql-client
    
RUN docker-php-ext-install pdo_mysql 
RUN docker-php-ext-install mysqli
COPY apache-config.conf /etc/apache2/sites-available/000-default.conf
COPY start-apache /usr/local/bin
RUN a2enmod rewrite

# Copy application source
ADD html/. /var/www
RUN chown -R www-data:www-data /var/www

CMD ["start-apache"]