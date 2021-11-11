FROM php:7.1-apache
COPY . /elgg-docker/
COPY docker_config/php.ini /usr/local/etc/php/

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        netcat \
        mysql-client \
        wget \
        unzip

# Elgg requirements
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install gd
RUN docker-php-ext-install pdo pdo_mysql
RUN docker-php-ext-install mbstring
RUN chmod +x /elgg-docker/composer-install.sh && /elgg-docker/composer-install.sh 

WORKDIR /var/www/html/

#Configs apache
RUN a2enmod rewrite

#Set time zone in server
ENV TIMEZONE="America/Sao_Paulo"
RUN cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime
#Set time zone in PHP
RUN sed -i "s#{{timezone}}#$TIMEZONE#g" /usr/local/etc/php/php.ini

# Database
ENV ELGG_DB_HOST=${ELGG_DB_HOST:-"mysql"}
ENV ELGG_DB_USER=$MYSQL_USER
ENV ELGG_DB_PASS=$MYSQL_PASS
ENV ELGG_DB_NAME=${ELGG_DB_NAME:-"elgg"}
ENV ELGG_DB_PORT=${MYSQL_PORT:-"3306"}
ENV ELGG_DB_PREFIX=${ELGG_DB_PREFIX:-"elgg_"}

# Elgg admin account
ENV ELGG_DISPLAY_NAME=${ELGG_DISPLAY_NAME:-"Admin"}
ENV ELGG_EMAIL=${ELGG_EMAIL:-"admin@myelgg.com"}
ENV ELGG_USERNAME=${ELGG_USERNAME:-"admin"}
ENV ELGG_PASSWORD=${ELGG_PASSWORD:-"admin-pass"}

ENV ELGG_SITE_NAME=${ELGG_SITE_NAME:-"Elgg Site"}
ENV ELGG_DATA_ROOT=${ELGG_DATA_ROOT:-"/media/elgg/"}
ENV ELGG_WWW_ROOT=${ELGG_WWW_ROOT:-"http://localhost:8000"}
ENV ELGG_SITE_ACCESS=${ELGG_SITE_ACCESS:-"2"}
ENV ELGG_PATH=${ELGG_PATH:-"/var/www/html/"}

RUN chmod +x /elgg-docker/elgg-install.sh