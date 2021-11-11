FROM ubuntu:trusty
MAINTAINER Bernhard Zürn <bernhard.zuern@gmail.com>

# Us bash as default-shell
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install packages
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -yq  --no-install-recommends install \
        apache2 \
        graphicsmagick \
        libapache2-mod-php5 \
        php5-curl \
        php5-gd \
        php5-mysql \
        php5-xmlrpc \
        php-apc \
        php5-mcrypt \
        php5-cli \
        mysql-client \
        wget \
        curl \
        pwgen \
        vim \
        git

# Install composer
RUN curl -sS https://getcomposer.org/installer --insecure | php -- --install-dir=/usr/local/bin --filename=composer

# Enable xdebug after composer
RUN apt-get -yq --no-install-recommends install php5-xdebug
ADD xdebug_settings.ini /etc/php5/mods-available/
RUN php5enmod xdebug_settings
RUN php5enmod mcrypt

# install zend guard loader
ADD docker/zend-loader-php5.5-linux-x86_64/ZendGuardLoader.so /usr/lib/php5/20121212/ZendGuardLoader.so
ADD docker/zend-loader-php5.5-linux-x86_64/opcache.so /usr/lib/php5/20121212/opcache.so
RUN echo zend_extension=/usr/lib/php5/20121212/ZendGuardLoader.so > /etc/php5/apache2/php.ini
#RUN echo zend_extension=/usr/lib/php5/20121212/opcache.so > /etc/php5/apache2/php.ini
RUN echo zend_extension=/usr/lib/php5/20121212/ZendGuardLoader.so > /etc/php5/cli/php.ini
#RUN echo zend_extension=/usr/lib/php5/20121212/opcache.so > /etc/php5/cli/php.ini

# config to enable .htaccess
#RUN service apache2 stop
ADD apache_default /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite

# Environment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M

# Environment variables to configure xdebug
ENV REMOTE_CONNECT_BACK 1
ENV REMOTE_HOST 127.0.0.1

CMD service apache2 restart && tail -f /var/log/apache2/error.log

EXPOSE 80 22
