FROM debian:squeeze
MAINTAINER Fuyuan Cheng <gloomcheng@netivism.com.tw>

# Use lenny repository for PHP 5.2.17.
RUN echo "deb http://archive.debian.org/debian lenny main contrib non-free" >> /etc/apt/sources.list
ADD sources/lenny /etc/apt/preferences.d/
RUN apt-get update \
    && apt-get install -y \
        apache2 \
        libapache2-mod-php5 \
        php5-common \
        php5-curl \
        php5-gd \
        php5-mcrypt \
        php5-mysql \
        php5-curl \
        curl \
        lynx-cur \
        wget \
        vim

# Install MySQL server and client.
RUN apt-get install -y \
     mysql-server \
     mysql-client
#ADD sources/create_user.sql /
CMD exec /usr/bin/mysqld_safe

# Enable apache mods.
RUN a2enmod php5
RUN a2enmod rewrite

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Update the default apache site with the config we created.
ADD sources/apache-config.conf /etc/apache2/sites-enabled/000-default

# By default, simply start mysql and apache.
EXPOSE 80
CMD /usr/sbin/apache2ctl -D FOREGROUND
