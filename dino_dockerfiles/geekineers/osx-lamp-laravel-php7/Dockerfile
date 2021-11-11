FROM ubuntu:16.04

MAINTAINER developers@8layertech.com

ENV DEBIAN_FRONTEND noninteractive

#Set variables
ENV DBUSER=root
ENV DBPASS=root
ENV APPPORT=4567

# START: FIX OSX permissions
ENV BOOT2DOCKER_ID 1000
ENV BOOT2DOCKER_GID 50

# Tweaks to give Apache/PHP write permissions to the app
RUN usermod -u ${BOOT2DOCKER_ID} www-data && \
    usermod -G staff www-data
RUN groupmod -g $(($BOOT2DOCKER_GID + 10000)) $(getent group $BOOT2DOCKER_GID | cut -d: -f1)
RUN groupmod -g ${BOOT2DOCKER_GID} staff
# END: FIX OSX permissions

# Update repo and install lamp, php, php dependencies, and phpmyadmin
RUN apt-get update --fix-missing && \
    apt-get -y install apt-utils && \
    apt-get -y install debconf-utils

RUN echo "mysql-server mysql-server/root_password password $DBUSER" | debconf-set-selections && \
    echo "mysql-server mysql-server/root_password_again password $DBPASS" | debconf-set-selections && \
    apt-get -y install mysql-server php-mysql apache2 \
                        php libapache2-mod-php php-mcrypt php-cli php-mbstring\
                        curl git supervisor --fix-missing

RUN service mysql restart 
RUN service apache2 restart

RUN echo "phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2" | debconf-set-selections && \
    echo "phpmyadmin phpmyadmin/dbconfig-install boolean true" | debconf-set-selections && \
    echo "phpmyadmin phpmyadmin/mysql/admin-user string $DBUSER" | debconf-set-selections && \
    echo "phpmyadmin phpmyadmin/mysql/admin-pass password $DBPASS" | debconf-set-selections && \
    echo "phpmyadmin phpmyadmin/mysql/app-pass password $DBPASS" | debconf-set-selections && \
    echo "phpmyadmin phpmyadmin/app-password-confirm password $DBPASS" | debconf-set-selections && \
    apt-get -y install phpmyadmin --fix-missing

RUN apt-get -y install zip && \
    apt-get -y install unzip

# Needs to be activated manually (that's an issue for Ubuntu 14.04)
# RUN phpenmod mcrypt

COPY app.local.conf /etc/apache2/sites-available/app.local.conf

#This will only work with GNU sed
RUN sed -i.bak "s/Listen 80/Listen 80\n\nListen $APPPORT\n/" /etc/apache2/ports.conf

RUN a2ensite 000-default && \
    a2ensite app.local && \
    a2enmod rewrite

# Downloading and installing curl
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Laravel install
RUN composer global require "laravel/installer"

EXPOSE 80
EXPOSE 4567

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD supervisord
