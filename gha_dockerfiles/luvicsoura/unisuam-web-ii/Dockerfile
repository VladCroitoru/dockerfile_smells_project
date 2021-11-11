FROM php:8.0.9-apache

WORKDIR /var/www/html

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive 

# Install systemd for sanity sake
# RUN apt-get install systemd

# Install MariaDB client
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y mariadb-client \ 
    && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    && apt-get install 

RUN a2enmod rewrite

COPY . /var/www/html/

# Install php-mysql driver
RUN docker-php-ext-install mysqli pdo pdo_mysql

CMD ["sh", "./init.sh"]