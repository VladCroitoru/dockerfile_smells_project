FROM php:5-apache
ARG SOURCE_BRANCH=dev

WORKDIR /var/www

RUN echo "ServerName z720.net" | tee /etc/apache2/conf-available/fqdn.conf
RUN a2enconf fqdn
RUN a2enmod rewrite
RUN a2enmod headers

RUN apt-get update && apt-get install -y git --no-install-recommends && apt-get clean

RUN mkdir -p /var/www/cache/oEmbed /var/www/cache/twig

COPY vendor /var/www/vendor
COPY html /var/www/html
COPY deploy.sh /var/www
COPY config /var/www/config

RUN echo "$SOURCE_BRANCH" | tee /var/www/build

RUN chown -R www-data:www-data /var/www/*
