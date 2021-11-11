FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -yq --no-install-recommends \
    apt-utils \
    curl \
    # Install git
    git \
    # Install apache
    apache2 \
    # Install php 7.2
    libapache2-mod-php7.2 \
    php7.2-cli \
    php7.2-json \
    php7.2-curl \
    php7.2-fpm \
    php7.2-gd \
    php7.2-ldap \
    php7.2-mbstring \
    php7.2-mysql \
    php7.2-soap \
    php7.2-sqlite3 \
    php7.2-xml \
    php7.2-zip \
    php7.2-intl \
    # Install tools
    openssl \
    nano \
    mysql-client \
    iputils-ping \
    locales \
    sqlite3 \
    apt-transport-https \
    ca-certificates \
    software-properties-common \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    #Update Cert Store
    && update-ca-certificates \
    # Set locales
    && locale-gen en_US.UTF-8 en_GB.UTF-8 de_DE.UTF-8 es_ES.UTF-8 fr_FR.UTF-8 it_IT.UTF-8 km_KH sv_SE.UTF-8 fi_FI.UTF-8 \
    && a2enmod rewrite expires php7.2

# Update the PHP.ini file, enable <? ?> tags and quieten logging.
ADD php.ini /etc/php/7.2/apache2/conf.d/
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.2/apache2/conf.d/php.ini \
&& sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php/7.2/apache2/conf.d/php.ini

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Configure vhost
ADD 00-gibbon.conf /etc/apache2/sites-enabled/00-gibbon.conf

EXPOSE 80

# By default start up apache in the foreground, override with /bin/bash for interactive.
CMD /usr/sbin/apache2ctl -D FOREGROUND
