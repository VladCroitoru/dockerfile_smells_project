FROM php:5.6-apache

# Get dependencies for PrestaShop
RUN apt-get update \
	&& apt-get install -y libmcrypt-dev \
	libjpeg62-turbo-dev \
	libpng-dev \
	libfreetype6-dev \
	libxml2-dev \
	&& rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install iconv mcrypt opcache pdo mysql pdo_mysql mbstring soap gd zip

# Apache configuration
RUN a2enmod rewrite
RUN chown -R www-data:www-data /var/www/html/
RUN usermod -u 1000 www-data

# PHP configuration
COPY ./php.ini /usr/local/etc/php/
