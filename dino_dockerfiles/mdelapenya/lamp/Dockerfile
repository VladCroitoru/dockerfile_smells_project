FROM debian:jessie
MAINTAINER Manuel de la Peña <manuel.delapenya@liferay.com>

# Install packages
ENV DEBIAN_FRONTEND noninteractive
RUN echo 'deb http://repo.mysql.com/apt/debian jessie mysql-5.7' > /etc/apt/sources.list.d/mysql-5.7.list && \
  gpg --export 5072E1F5 > /etc/apt/trusted.gpg.d/5072E1F5.gpg && \
  gpg --recv-keys 5072E1F5 && \
  gpg --export 5072E1F5 > /etc/apt/trusted.gpg.d/5072E1F5.gpg && \
  apt-get update && \
  apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server="5.7.17-1debian8" php5-mysql pwgen php-apc php5-mcrypt && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  echo "ServerName localhost" >> /etc/apache2/apache2.conf

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
RUN chmod 755 /*.sh

# config to enable .htaccess
ADD apache_default /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite

# Configure /app folder with sample app
RUN git clone https://github.com/fermayo/hello-world-lamp.git /app
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html

#Environment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M

# Add volumes for MySQL 
VOLUME  ["/etc/mysql", "/var/lib/mysql" ]

EXPOSE 80 3306
CMD ["/run.sh"]
