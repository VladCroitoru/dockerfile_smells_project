# Based on occitech/cakephp and tutum/lamp. All credit goes there!
FROM ubuntu:trusty
MAINTAINER xymanek <xymanek@outlook.com>

ENV DEBIAN_FRONTEND noninteractive
ENV MYSQL_ROOT_PASS root

RUN echo mysql-server mysql-server/root_password password $MYSQL_ROOT_PASS | debconf-set-selections
RUN echo mysql-server mysql-server/root_password_again password $MYSQL_ROOT_PASS | debconf-set-selections

RUN apt-get update && \
  apt-get -y install git apache2 libapache2-mod-php5 mysql-server php5-mysql pwgen php-apc php5-mcrypt

# config to enable .htaccess
ADD apache_default /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite

# Add volumes for MySQL 
VOLUME  ["/etc/mysql", "/var/lib/mysql" ]

RUN service mysql restart

EXPOSE 80 3306

RUN requirements="libmcrypt-dev g++ libicu-dev libmcrypt4 libicu52 curl php5-mcrypt php5-intl php5-curl" \
    && apt-get update && apt-get install -y $requirements \
    && requirementsToRemove="libmcrypt-dev g++ libicu-dev" \
    && apt-get purge --auto-remove -y $requirementsToRemove \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && apt-get update \
    && apt-get install -y zlib1g-dev git \
    && apt-get purge -y --auto-remove zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN a2enmod rewrite

RUN usermod -u 1000 www-data
