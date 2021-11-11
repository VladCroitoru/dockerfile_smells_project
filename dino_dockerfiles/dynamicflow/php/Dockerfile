FROM ubuntu:16.04
MAINTAINER Alessandro Oliveira <alessandro@dynamicflow.com.br>

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y curl \
                       git \
                       php \
                       php-mcrypt \
                       php-gd \
                       php-mbstring \
                       php-xml \
                       php-mysql \
                       php-redis \
                       php-curl \
                       php7.0-zip \
                       apache2 \
                       libapache2-mod-php && \
    rm -rf /var/lib/apt/* && \
    rm -rf /var/cache/apt/* && \
    rm /etc/apache2/sites-enabled/* && \
    rm -rf /var/www/html && \
    a2enmod rewrite && \
    a2enmod ssl && \
    a2enmod headers

RUN curl -sS https://getcomposer.org/installer | php -- args --install-dir=/usr/local/bin --filename composer

ENV APACHE_PID_FILE=/var/run/apache2/apache2.pid
ENV APACHE_RUN_USER=www-data
ENV APACHE_LOG_DIR=/var/log/apache2
ENV APACHE_RUN_GROUP=www-data
ENV APACHE_RUN_DIR=/var/run/apache2
ENV APACHE_LOCK_DIR=/var/lock/apache2
