FROM php:8-apache
MAINTAINER dieKeuleCT<koehlmeier@gmail.com>
# install apt-utils since there seems to be an issue with the base image
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y --no-install-recommends apt-utils
# install some extensions
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libxml2 \
        libxml2-dev \
        libicu-dev \
        wget \
        mariadb-client \
        unzip \
        git \
        cron \
        vim \
        inetutils-syslogd \
        libxrender1 \
        libfontconfig1 \
        libapache2-mod-rpaf \
        logrotate \
        libzip-dev \
        default-mta \
    && docker-php-ext-install -j$(nproc) mysqli iconv intl opcache pdo pdo_mysql soap xml zip \
    && docker-php-ext-configure gd  \
    && docker-php-ext-install -j$(nproc) gd
# removed because of error mbstring (should already be included by default) #--with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
# adding some configurations for apache, php
ADD wkhtmltopdf /usr/local/bin/wkhtmltopdf
ADD wkhtmltoimage /usr/local/bin/wkhtmltoimage
ADD wkhtmltox/lib/libwkhtmltox.so /usr/local/lib/libwkhtmltox.so
ADD wkhtmltox/lib/libwkhtmltox.so.0 /usr/local/lib/libwkhtmltox.so.0
ADD wkhtmltox/lib/libwkhtmltox.so.0.12 /usr/local/lib/libwkhtmltox.so.0.12
ADD wkhtmltox/lib/libwkhtmltox.so.0.12.3 /usr/local/lib/libwkhtmltox.so.0.12.3
ADD php.ini /usr/local/etc/php/php.ini
ADD apache2.conf /etc/apache2/apache2.conf
ADD logrotate-apache2 /etc/logrotate.d/apache2
ADD symfony-apache.conf /etc/apache2/sites-available/000-default.conf
ADD main.cf /etc/postfix/main.cf
ADD startup.sh /usr/local/startup.sh
ADD composer-setup.sh /usr/local/composer-setup.sh
# Enable rewrite and install composer for use in symfony
RUN a2enmod rewrite && a2enmod rpaf && a2enmod ssl 
RUN chmod a+x /usr/local/composer-setup.sh && /usr/local/composer-setup.sh && chmod a+x /usr/bin/composer && chmod +x /usr/local/startup.sh

CMD "/usr/local/startup.sh"
