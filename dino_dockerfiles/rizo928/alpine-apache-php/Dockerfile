#
# Alpine linux docker image
#
# An image based on Alpine Linux with Apache2, PHP5, Composer, various PHP extensions and useful utilities.
#
# Concepts originally taken from gliderlabs/alpine
#

FROM alpine:latest

MAINTAINER Jerald Watts <proxy@silverforge.net>

# Set environment variables.
ENV \
  TERM=xterm-color

# Install packages.
RUN \
  apk add --update --no-cache \
    bash \
    coreutils \
    curl \
    nano \
    vim \
    git \
    tar \
    openssh-client\
    ssmtp \
    wget
    
#############
# TBD Use environment variable to specify which php modules to load beyond the bare basics
#
RUN apk add --update --no-cache \
    php7 \
    php7-dev \
    php7-apache2 \
    php7-iconv \
    php7-json \
    php7-phar \
    php7-openssl \
    php7-xml \
    php7-xsl \
    php7-dom \
    php7-curl \
    php7-pear \
    php7-mbstring \
    php7-pdo \
    php7-ctype \
    php7-session \
    && rm -rf /var/cache/apk/*

RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories
RUN apk add --update --no-cache php7-mongodb@testing\
    && rm -rf /var/cache/apk/*
    
RUN ln -s /usr/bin/php7 /usr/local/bin/php
RUN mv /usr/sbin/sendmail /usr/sbin/sendmail.! \
    && ln -s /usr/sbin/ssmtp /usr/sbin/sendmail

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN mkdir /app \
    && mkdir /run/apache2 \
    && chown -R apache:apache /run/apache2 \
    && chown -R apache:apache /app \
    && sed -i 's#^DocumentRoot ".*#DocumentRoot "/app"#g' /etc/apache2/httpd.conf \
    && sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/httpd.conf \
    && sed -i 's/Options Indexes FollowSymLinks/Options FollowSymLinks/' /etc/apache2/httpd.conf \
    && sed -i 's/#LoadModule rewrite_module/LoadModule rewrite_module/' /etc/apache2/httpd.conf \
    && sed -i 's#/var/www/localhost/htdocs#/#' /etc/apache2/httpd.conf
    
# RUN sed -i 's/#ServerName www.example.com:80/ServerName myserver.com/' /etc/apache2/httpd.conf

RUN sed -i 's#-n##' /usr/bin/pecl

RUN sed -i 's/;zend.multibyte = Off/zend.multibyte = On/' /etc/php7/php.ini
RUN sed -i 's/;include_path = \".:\/php\/includes\"/include_path = \".:\/usr\/share\/php7\"/' /etc/php7/php.ini

RUN sed -i 's/;date.timezone =/date.timezone = America\/New_York/' /etc/php7/php.ini

COPY run.sh /run.sh
RUN chown root:root /run.sh
RUN chmod 755 /run.sh

EXPOSE 80

# VOLUME /app
WORKDIR /app

# This will run any scripts found in /scripts/*.sh
# then start Apache
ENTRYPOINT ["/run.sh"]
