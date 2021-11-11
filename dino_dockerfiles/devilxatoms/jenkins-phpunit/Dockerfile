FROM jenkins:latest
MAINTAINER Brayan Caldera <ing.brayan.cm@gmail.com>

# Jenkins is using jenkins user, we need root to install things.
USER root

# Install php packages.
RUN apt-get update
RUN apt-get -y -f install php7.0 php7.0-fpm php-xml

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
