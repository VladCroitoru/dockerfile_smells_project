# All rights reserved © 2018 Zero
FROM php:7.2.2-apache
MAINTAINER Mohos Tamas <tomi@mohos.name>

ENV DEBIAN_FRONTEND="noninteractive"

# Update and install required packages
RUN apt-get update \
    && apt-get -y dist-upgrade \
    && apt-get install -y git curl cron zlib1g-dev libicu-dev g++ rsyslog nano \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-install zip

# Config
RUN rm -f /etc/localtime \
    && ln -s /usr/share/zoneinfo/Europe/Budapest /etc/localtime \
    && echo "Europe/Budapest" > /etc/timezone \
    && echo "log_errors = On" >> /usr/local/etc/php/php.ini \
    && echo "error_log = /dev/stderr" >> /usr/local/etc/php/php.ini \
    && echo "date.timezone = 'Europe/Budapest'" >> /usr/local/etc/php/php.ini \
    && echo "ServerName localhost" >> /etc/apache2/apache2.conf \
    && a2enmod rewrite
   
# Install binaries
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && cd /var/www \
    && composer create-project composer/satis --stability=dev --keep-vcs \
	&& mkdir -p /root/.ssh \
	&& sed -i "s/#   StrictHostKeyChecking ask/    StrictHostKeyChecking no/" /etc/ssh/ssh_config
 
# Define workspace
WORKDIR /var/www/satis


