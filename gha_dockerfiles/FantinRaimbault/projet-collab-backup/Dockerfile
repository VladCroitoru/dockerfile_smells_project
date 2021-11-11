FROM php:8-apache
ENV COMPOSER_ALLOW_SUPERUSER=1
EXPOSE 80
WORKDIR /site/
RUN apt-get update && apt-get install -y libzip-dev zip libmemcached-dev libcurl4-openssl-dev zlib1g-dev\
    && docker-php-ext-install curl pdo pdo_mysql zip\
    && pecl install memcached\
    && docker-php-ext-enable memcached\
    && curl -sS https://getcomposer.org/installer | php\
    && mv composer.phar /usr/local/bin/\
    && ln -s /usr/local/bin/composer.phar /usr/local/bin/composer
RUN pecl install xdebug \
    && docker-php-ext-enable xdebug
COPY ./site /site 
COPY ./vhost.conf /etc/apache2/sites-available/000-default.conf
COPY ./apache.conf /etc/apache2/conf-available/z-app.conf
COPY ./php.ini /usr/local/etc/php/conf.d/app.ini
RUN a2enmod rewrite remoteip && \
    a2enconf z-app
RUN composer update
RUN cp /usr/local/etc/php/php.ini-development /usr/local/etc/php/php.ini
RUN composer install --no-interaction
ENTRYPOINT ["apache2-foreground"]