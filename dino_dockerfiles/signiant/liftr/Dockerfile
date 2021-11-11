FROM php:5.6-apache

# LDAP requirements
RUN apt-get update && \
    apt-get install -y git ldap-utils libldap2-dev && \
    rm -rf /var/lib/apt/lists/* && \
    docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \
    docker-php-ext-install ldap

# Install Composer and make it available in the PATH
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

COPY src/ /var/www/html/

WORKDIR /var/www/html/

RUN composer install --prefer-source --no-interaction
