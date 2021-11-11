FROM php:7.4-apache
WORKDIR /var/www/html

COPY . .
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer
RUN composer install --no-dev

RUN docker-php-ext-install mysqli pdo pdo_mysql && docker-php-ext-enable pdo_mysql

RUN a2enmod rewrite &&\
    service apache2 restart
RUN chown -R www-data:www-data /var/www/html &&\
    chmod -R g+rw /var/www/html
	
EXPOSE 80
