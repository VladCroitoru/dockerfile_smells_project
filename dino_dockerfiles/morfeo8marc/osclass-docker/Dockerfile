FROM ubuntu:trusty

MAINTAINER Marc Navarro https://github.com/morfeo8marc

# Install packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server php5-mysql pwgen php-apc php5-mcrypt php5-gd

# Add image configuration and scripts
ADD start-apache2.sh /start-apache2.sh
ADD start-mysqld.sh /start-mysqld.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
ADD my.cnf /etc/mysql/conf.d/my.cnf
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf

# Remove pre-installed database
RUN rm -rf /var/lib/mysql/*

# Add MySQL utils
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
ADD osclass_init.sh /osclass_init.sh
RUN chmod 755 /*.sh

# config to enable .htaccess
ADD apache_default /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite

# Configure /app folder with Osclass forked codebase.
# The forked repository is used to avoid authentication error in theme-bender git submodule
RUN git clone --recursive https://github.com/morfeo8marc/Osclass.git /app 
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html 

#Enviornment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M

# Add volumes for MySQL 
VOLUME  ["/etc/mysql", "/var/lib/mysql" ]

#Added to avoid in container connection to the database with mysql client error message "TERM environment variable not set"
ENV TERM dumb

EXPOSE 80 3306
CMD ["/run.sh"]
