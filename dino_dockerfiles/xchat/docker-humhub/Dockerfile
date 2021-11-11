# Humhub
#
# VERSION               0.0.1
#


FROM     ubuntu
MAINTAINER Jerry Li

ENV DEBIAN_FRONTEND noninteractive
ENV GIT_MASTER_URL https://github.com/humhub/humhub/archive/master.zip
ENV ROOT_PASSWORD rboDlyGo!
ENV DB_ROOT_PASSWORD dboDlyGo!
ENV DB_DATABASE humhub
ENV DB_USER humhub
ENV DB_PASSWORD _HuMhUb!

# updates

RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q && apt-get -y -q autoclean && apt-get -y -q autoremove)

# supervisord

RUN apt-get install -y supervisor
RUN service supervisor restart

# lamp

ADD configs/lamp/lamp-install.sh /lamp-install.sh
RUN chmod 750 /lamp-install.sh
RUN (/bin/bash -c /lamp-install.sh)

# apache

ADD configs/mysql/start-mysqld.sh /start-mysqld.sh
ADD configs/apache/start-apache2.sh /start-apache2.sh
RUN chmod 750 /start-mysqld.sh
RUN chmod 750 /start-apache2.sh
ADD configs/mysql/my.cnf /etc/mysql/conf.d/my.cnf

# Remove pre-installed database
# this seems to cause issues?
#RUN rm -rf /var/lib/mysql/*

# Add volumes for MySQL

VOLUME  ["/etc/mysql", "/var/lib/mysql" ]

# neccessary packages install
RUN apt-get install -y -q php5-gd php5-curl php5-sqlite php5-ldap php-apc wget unzip cron curl

# install composer
RUN curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer

RUN wget $GIT_MASTER_URL
RUN unzip master.zip
RUN mv humhub-master /var/www/humhub
RUN chown www-data:www-data -R /var/www/

RUN cd /var/www/humhub

# install humhub dependencies
RUN composer global require "fxp/composer-asset-plugin:~1.1.0"
RUN composer update

# config

ADD configs/apache/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
ADD configs/humhub/pre-conf.sh /pre-conf.sh
RUN chmod +x /pre-conf.sh
RUN (/bin/bash -c /pre-conf.sh)
RUN service apache2 stop
RUN a2enmod ssl
RUN a2enmod rewrite
RUN a2dissite 000-default
RUN a2ensite default-ssl

# openssh

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
ADD configs/openssh/openssh-conf.sh /openssh-conf.sh
ADD configs/openssh/start-openssh.sh /start-openssh.sh
RUN chmod 750 /start-openssh.sh
RUN chmod 750 /openssh-conf.sh
RUN (/bin/bash -c /openssh-conf.sh)
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# phpmyadmin

ADD configs/phpmyadmin/pre-phpmyadmin-setup.sh /pre-phpmyadmin-setup.sh
RUN chmod +x /pre-phpmyadmin-setup.sh
RUN /pre-phpmyadmin-setup.sh
RUN apt-get install phpmyadmin -y
ADD configs/phpmyadmin/config.inc.php /etc/phpmyadmin/conf.d/config.inc.php
RUN chmod 755 /etc/phpmyadmin/conf.d/config.inc.php
ADD configs/phpmyadmin/phpmyadmin-setup.sh /phpmyadmin-setup.sh
RUN chmod +x /phpmyadmin-setup.sh
RUN /phpmyadmin-setup.sh

# start services

ADD configs/mysql/supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf
ADD configs/apache/supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf
ADD configs/openssh/supervisord-openssh.conf /etc/supervisor/conf.d/supervisord-openssh.conf
ADD configs/humhub/supervisord-humhub.conf /etc/supervisor/conf.d/supervisord-humhub.conf

EXPOSE 22 80 443 3306 30000-30009
CMD ["supervisord", "-n"]
