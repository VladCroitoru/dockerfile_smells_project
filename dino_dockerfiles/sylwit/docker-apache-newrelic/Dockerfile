FROM php:7.2-apache

ENV TERM xterm-256color
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends wget gnupg

RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee /etc/apt/sources.list.d/newrelic.list \
    && wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add -

RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        locales \
        imagemagick \
        ghostscript \
        libmagickwand-dev \
        newrelic-php5 \
	supervisor \
    && docker-php-ext-install -j$(nproc) mbstring pdo pdo_mysql mysqli \
    && a2enmod rewrite \
    && apt-get autoremove -y && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo "America/New_York" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

RUN pecl install imagick redis \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable imagick redis

ARG NR_INSTALL_SILENT=1
RUN newrelic-install install \
    && sed -i \
        -e "s/newrelic.license =.*/newrelic.license = \${NEW_RELIC_LICENSE_KEY}/" \
        -e "s/newrelic.appname =.*/newrelic.appname = \${NEW_RELIC_APP_NAME}/" \
        /usr/local/etc/php/conf.d/newrelic.ini

RUN rm -Rf /var/www/html

WORKDIR /var/www
