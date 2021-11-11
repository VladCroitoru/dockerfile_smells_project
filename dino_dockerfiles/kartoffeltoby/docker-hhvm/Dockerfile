FROM debian:jessie
MAINTAINER Tobias Haber <kontakt@t-haber.de>

RUN echo "Europe/Berlin" > /etc/timezone 
RUN export LANGUAGE=de_DE.UTF-8 && \
      export LANG=de_DE.UTF-8 && \
      export LC_ALL=de_DE.UTF-8 && \
      DEBIAN_FRONTEND=noninteractive

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_SERVERADMIN admin@localhost
ENV APACHE_SERVERNAME localhost
ENV APACHE_SERVERALIAS docker.localhost
ENV APACHE_DOCUMENTROOT /var/www

#Add non-free deb
RUN echo "deb http://ftp.de.debian.org/debian/ jessie non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://ftp.de.debian.org/debian/ jessie non-free" >> /etc/apt/sources.list

#Install Main Services HHVM
RUN apt-get update -y && \
      apt-get install -y wget && \
      apt-get update -y && \
      apt-get install -y -f apache2 apache2-utils libapache2-mod-fastcgi && \
      wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | apt-key add - && \
      echo deb http://dl.hhvm.com/debian jessie main | tee /etc/apt/sources.list.d/hhvm.list && \
      apt-get update -y && \
      apt-get install libgmp10 libmemcachedutil2 software-properties-common python-software-properties python-setuptools drush curl mysql-client unzip wget wget curl build-essential ghostscript-x graphicsmagick-imagemagick-compat libgoogle-perftools-dev libelf-dev libdwarf-dev libfcgi-dev libfcgi0ldbl libjpeg62-turbo-dbg libmcrypt-dev libssl-dev libc-client2007e libc-client2007e-dev libxml2-dev libbz2-dev libcurl4-openssl-dev libjpeg-dev libpng12-dev libfreetype6-dev libkrb5-dev libpq-dev libxml2-dev libxslt1-dev libxml2-dev graphicsmagick build-essential perl libcurl4-openssl-dev libjpeg-dev libpng-dev libxpm-dev libmysqlclient-dev libpq-dev libicu-dev libfreetype6-dev libldap2-dev libxslt-dev -y && \
      apt-get install -fy hhvm-nightly



### PHP 7 ###
RUN echo "deb http://repos.zend.com/zend-server/early-access/php7/repos ubuntu/" >> /etc/apt/sources.list
RUN apt-get update -y && apt-get install php7-nightly --force-yes -y
RUN cp /usr/local/php7/libphp7.so /usr/lib/apache2/modules/
RUN cp /usr/local/php7/php7.load /etc/apache2/mods-available/
RUN ln -sf /usr/local/php7/bin/php /usr/bin/php
ADD ./php.ini /usr/local/php7/etc/php.ini

### APACHE2 Mods ###
RUN a2dismod mpm_event
RUN a2enmod mpm_prefork
RUN a2enmod php7
RUN a2enmod rewrite
RUN a2enmod actions fastcgi alias
RUN a2enmod proxy_fcgi
RUN a2enmod proxy

### PAGESPEED ####
RUN wget https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-beta_current_amd64.deb
RUN dpkg -i mod-pagespeed-*.deb
RUN rm -f mod-pagespeed-*.deb
RUN apt-get -f install -y
RUN chown 999.999 /var/cache/mod_pagespeed
RUN chown 999.999 /var/log/pagespeed
ADD ./pagespeed.conf /etc/apache2/mods-enabled/pagespeed.conf


### Add Configs ###
ADD ./app.conf /etc/apache2/sites-available/app.conf
RUN rm /etc/apache2/sites-enabled/*
RUN ln -s /etc/apache2/sites-available/app.conf /etc/apache2/sites-enabled/app.conf

### Fixing Shit ###
RUN echo "hhvm.server.fix_path_info = true" >> /etc/hhvm/server.ini

### www dir (app for CMS) ###
ADD  ./info.php /var/www/index.php
RUN  chown -R www-data:www-data /var/www

### Cleanup ###
RUN  apt-get autoremove
RUN  apt-get autoclean
RUN  apt-get clean
RUN  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

### Startup Script ###
ADD ./start.sh /start.sh
RUN  chmod +x /start.sh
RUN  /usr/share/hhvm/install_fastcgi.sh

#GOGO

EXPOSE 80
CMD ./start.sh
