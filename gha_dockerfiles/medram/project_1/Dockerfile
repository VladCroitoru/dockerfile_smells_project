FROM php:7.3-apache

WORKDIR /var/www/html

# installing php composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
	&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
	&& php -r "unlink('composer-setup.php');"

RUN apt-get update && apt-get upgrade -y \
	&& apt-get install -y libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libmcrypt-dev \
        libicu-dev \
	    libxml2-dev \
	    iputils-ping \
	    git \
	    curl \
	    wget \
	    unzip \
	&& apt-get clean

RUN pecl install mcrypt \
	&& docker-php-ext-install -j$(nproc) mysqli pdo pdo_mysql mbstring gd xml \
	&& docker-php-ext-enable mysqli pdo pdo_mysql mbstring mcrypt xml gd \
	&& a2enmod rewrite

# Fixing permissions.
RUN chown -R www-data:www-data /var/www/html \
	&& find /var/www/html -type d -exec chmod 775 {} \; \
	&& find /var/www/html -type f -exec chmod 664 {} \;

# creating/switching from root to a user.
USER www-data

COPY --chown=www-data:www-data . .

#COPY composer.* ./
RUN composer install --no-cache

EXPOSE 80
