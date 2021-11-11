FROM php:5.6-apache

RUN a2enmod rewrite

# install the PHP extensions we need
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev git && rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
	&& docker-php-ext-install gd mysqli zip


COPY php.ini /usr/local/etc/php/php.ini
COPY 000-default.conf /etc/apache2/sites-available

VOLUME /var/www
WORKDIR /var/www


CMD ["apache2-foreground"]