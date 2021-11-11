FROM php:7.2-apache-stretch

COPY ./src /var/www/html
COPY ./apache2/000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

RUN apt-get update && \
    apt-get install -qqy --no-install-recommends \
    git \
    unzip \
    zip \
    nano \
    libonig-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libaio1 \
    libpq-dev \
    libicu-dev \
    curl \
    ldap-utils \
    libldap2-dev \
    libmcrypt-dev \
    wget \
    mariadb-common \
    mariadb-server \
    mariadb-client

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# enable some of required extension for PHP
RUN docker-php-ext-install \
    mysqli \
    pdo \
    pdo_mysql \
    gd \
    ldap

RUN cd /var/www/html \
    && composer install \
    && cd db \
    && /bin/bash -c "/usr/bin/mysqld_safe --skip-grant-tables &" \
    && sleep 5 \
    && mysql -u root -e "CREATE DATABASE invsys_db" \
    && mysql -u root invsys_db < invsys_db.sql \ 
    && mysql -u root -e "FLUSH PRIVILEGES;CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';" \
    && a2enmod rewrite \
    && chmod +x /docker-entrypoint.sh

RUN apt-get clean autoclean && apt-get autoremove --yes &&  rm -rf /var/lib/{apt,dpkg,cache,log}/

EXPOSE 80

ENTRYPOINT "/docker-entrypoint.sh"