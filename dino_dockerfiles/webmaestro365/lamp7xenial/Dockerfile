# Version: 1.0.0
FROM ubuntu:xenial
# Based on tutum/lamp maintained by Fernando Mayo <fernando@tutum.co>, Feng Honglin <hfeng@tutum.co>
MAINTAINER A. Datta <intersoftbengal@ymail.com>
# Install packages (Modified by A. Datta)
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get -y install supervisor git apache2 php php-intl libapache2-mod-php7.0 mysql-server php7.0-mysql pwgen php-apcu php7.0-mcrypt && \
  echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Add image configuration and scripts
ADD start-apache2.sh /start-apache2.sh
ADD start-mysqld.sh /start-mysqld.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
# ADD my.cnf /etc/mysql/conf.d/my.cnf (Removed by A. Datta as location doesn't have precedence in current version)

ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf

# Remove pre-installed database
RUN rm -rf /var/lib/mysql/*

# Add MySQL utils
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
RUN chmod 755 /*.sh

# config to enable .htaccess
ADD apache_default /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite

# Configure /app folder with sample app
RUN git clone https://github.com/fermayo/hello-world-lamp.git /app
# Line added by A. Datta to update PHP code:
ADD index.php /app/
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html

#Environment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M

# Add volumes for MySQL 
VOLUME  ["/etc/mysql", "/var/lib/mysql" ]

EXPOSE 80 3306
CMD ["/run.sh"]
