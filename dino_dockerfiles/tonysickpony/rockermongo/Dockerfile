FROM debian:jessie

MAINTAINER tony fu

# Install Dev Tools
RUN apt-get update -yq              && \     
    apt-get install -yq                \
        apache2                        \
        php5-dev                       \
        libapache2-mod-php5            \
        wget                           \
        unzip

# Apache Environmet Variables
ENV APACHE_RUN_USER=www-data           \
    APACHE_RUN_GROUP=www-data          \
    APACHE_LOG_DIR=/var/log/apache2    \
    APACHE_LOCK_DIR=/var/lock/apache2

# Rockmongo Environment Variables
ENV MONGO_HOST=localhost               \
    MONGO_PORT=27017                   \
    MONGO_ADMIN_PASSWORD=password      \
    RM_URL=https://github.com/gilacode/rockmongo/archive/master.zip

# Install php Mongo Driver
RUN pecl install mongo              && \
    echo "extension=mongo.so" >> /etc/php5/apache2/php.ini

# Prepare Workdir
RUN rm /var/www/html/*
WORKDIR /var/www/html

# Install Rockmongo
RUN wget ${RM_URL} -O rockmongo.zip && \
    unzip rockmongo.zip -d .        && \
    mv ./rockmongo-master/* .

# Install Rockmongo Configuration
COPY config.php ./config.php

EXPOSE 80
EXPOSE 443

CMD ["apache2", "-D", "FOREGROUND"]
