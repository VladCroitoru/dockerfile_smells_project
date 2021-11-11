



FROM php:8.0.5-apache
RUN a2enmod rewrite



RUN apt-get update && apt-get install -y \
        zlib1g-dev \
        libicu-dev \
        libxml2-dev \
        libpq-dev \
        libzip-dev \
        && docker-php-ext-install pdo pdo_mysql zip intl xmlrpc soap opcache \
        && docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd


#RUN apt-get update -y 

# Add Node 8 LTS
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -- \
	&& apt-get install -y nodejs \
	&& apt-get autoremove -y

COPY --from=composer /usr/bin/composer /usr/bin/composer
COPY  docker/php.ini /usr/local/etc/php/
COPY  docker/apache/vhost.conf /etc/apache2/sites-available/000-default.conf
COPY  docker/apache/apache2.conf /etc/apache2/apache2.conf
#COPY  docker/.env-pro /var/htdocs/html/.env


ENV COMPOSER_ALLOW_SUPERUSER 1

#COPY  . /var/www/html/
#WORKDIR /var/www/html/

#UN chown -R www-data:www-data /var/htdocs/html  \
    #&& composer install  && composer dumpautoload 