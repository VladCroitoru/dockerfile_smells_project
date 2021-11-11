# First docker test, so this is a all in one docker file
FROM buildpack-deps:jessie
MAINTAINER Tibor Sári <tiborsari@gmx.de>

ENV DEBIAN_FRONTEND noninteractive

## add dotdeb to apt sources list
RUN echo 'deb http://packages.dotdeb.org jessie all' > /etc/apt/sources.list.d/dotdeb.list
RUN echo 'deb-src http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list.d/dotdeb.list

## add dotdeb key for apt
RUN curl http://www.dotdeb.org/dotdeb.gpg | apt-key add -

# pin the versions
COPY dotdeb.pin /etc/apt/preferences.d/php

# update, install and clean up to minimize the image size
RUN \
    apt-get update -qq && \
    apt-get install --no-install-recommends -y \
        apache2 \
        libapache2-mod-php7.0 \
        php7.0-mysql \
        php7.0-curl \
        php7.0-apcu \
        sudo \
    && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Enable apache mods.
RUN a2enmod php7.0 && a2enmod rewrite

# Update the PHP.ini file, enable <? ?> tags and quieten logging.
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.0/apache2/php.ini && \
    sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php/7.0/apache2/php.ini

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Update the default apache site with the config we created.
COPY apache-config.conf /etc/apache2/sites-enabled/000-default.conf

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set up the command arguments
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]