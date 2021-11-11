FROM davefx/trusty-php-selenium-headless:latest
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

MAINTAINER David Marín <david.marin@toptal.com>
RUN apt-get -y update
RUN apt-get install -y php5 mysql-server php5-mysqlnd php5-gd php5-json php5-apcu php5-intl php5-readline php5-xmlrpc php5-xsl memcached php5-memcached
RUN a2ensite default-ssl
RUN service apache2 start
RUN service mysql start

