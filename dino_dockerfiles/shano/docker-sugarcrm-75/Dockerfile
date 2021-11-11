FROM ubuntu:13.04

MAINTAINER Shane Dowling, shane@shanedowling.com

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV HOME /root

# Utilities and Apache, PHP
RUN echo "deb http://old-releases.ubuntu.com/ubuntu raring main restricted universe multiverse" > /etc/apt/sources.list &&\
    apt-get update &&\
    apt-get upgrade -y &&\
    DEBIAN_FRONTEND=noninteractive apt-get -y install git subversion curl apache2 php5 php5-cli libapache2-mod-php5 php5-mysql php-apc php5-gd php5-curl php5-memcached php5-mcrypt php5-mongo php5-sqlite mysql-client &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

RUN sed -i -r 's/AllowOverride None$/AllowOverride All/' /etc/apache2/apache2.conf

# PHP prod config
ADD files/php.ini /etc/php5/apache2/php.ini
ADD files/vhost.conf /etc/apache2/sites-available/sugarcrm

# Ensure PHP log file exists and is writable
RUN touch /var/log/php_errors.log && chmod a+w /var/log/php_errors.log

# Our start-up script
ADD files/start.sh /start.sh
RUN chmod a+x /start.sh

# Turn on some crucial apache mods
RUN a2enmod rewrite headers filter

RUN a2dissite 000-default
RUN a2ensite sugarcrm

RUN apache2ctl restart

VOLUME ["/var/www/sugarcrm"]
VOLUME ["/var/log"]

ENTRYPOINT ["/start.sh"]
EXPOSE 80
