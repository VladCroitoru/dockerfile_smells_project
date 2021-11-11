#~~~ INFORMATION ~~~#
# VERSION 1.0.0

# based on
# https://hub.docker.com/r/richarvey/nginx-php-fpm/
# and
# https://hub.docker.com/_/wordpress/

FROM php:5.6-apache

MAINTAINER Miquel Adell <miquel@miqueladell.com>

ENV WORDPRESS_VERSION 4.4.1 #can we do that dynamic?



#~~~ DEPENDENCIES ~~~#

# Add PHP repository to apt source
RUN \
        apt-get update \
    &&  apt-get install -y \
            libpng12-dev \
            libjpeg-dev  \
            curl \
            sed \
            zlib1g-dev \
            rsync \
    &&  docker-php-ext-install \
            gd \
            mysqli \
            opcache \
            zip \
    &&  docker-php-ext-configure \
            gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    &&  rm -rf /var/lib/apt/lists/*

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=60'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
	} > /usr/local/etc/php/conf.d/opcache-recommended.ini



#~~~ VOLUMES ~~~#

RUN mkdir /usr/src/wordpress
WORKDIR /usr/src/wordpress



#~~~ WORDPRESS ~~~#

COPY files/composer.json composer.json
RUN composer update

#~ COPY BASE FILES ~#
COPY files/.gitignore .gitignore
COPY files/index.php index.php
COPY files/wordpress/wp-config-custom.php wordpress/wp-config-custom.php

RUN chown -R www-data:www-data /usr/src/wordpress



#~~~ MOVE FILES TO THE VOLUME ~~~#

VOLUME /var/www/html/
WORKDIR /var/www/html/

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["apache2-foreground"]
