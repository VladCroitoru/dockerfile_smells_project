FROM ubuntu:14.04
MAINTAINER arfan@mylits.com

ENV DEBIAN_FRONTEND noninteractive

# install required packages
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-key E5267A6C

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    supervisor \
    apache2 \
    php5.6-fpm \
    php5.6-mysql \
    php5.6-gd \
    php5.6-curl \
    php5.6-xml \
    php5.6-mbstring \
    php5.6-zip \
    php5-cli \
    php5-gd \
    php5-mysql \
    php5-curl \
    curl \
    git \
    wget \
    unzip \
  && rm -r /var/lib/apt/lists/*

RUN a2enmod proxy
RUN a2enmod proxy_fcgi setenvif
RUN a2enconf php5.6-fpm

RUN mkdir -p /run/php/

# configure apache php5.6-fpm
COPY php5.6-fpm.conf /etc/apache2/conf-available/php5.6-fpm.conf
RUN sed -i 's/\/run\/php\/php5.6-fpm.sock/127.0.0.1:9000/g' /etc/php/5.6/fpm/pool.d/www.conf

COPY scripts /scripts
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# add phpinfo
RUN echo "<?php phpinfo();" >> /var/www/html/index.php

RUN mkdir /src
WORKDIR /src

# expose 3306 mysql port
EXPOSE 3306

CMD ["/usr/bin/supervisord"]