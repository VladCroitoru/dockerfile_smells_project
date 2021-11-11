FROM php:5.6-apache
RUN echo "America/Sao_Paulo" > /etc/timezone \
&& dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && apt-get install -y php5-mysql mysql-client zlib1g-dev libmcrypt-dev
RUN docker-php-ext-install -j$(nproc) zip mysqli mcrypt pdo_mysql sockets

RUN a2enmod rewrite

COPY php.ini /usr/local/etc/php/php.ini

EXPOSE 80
CMD ["apache2-foreground"]
