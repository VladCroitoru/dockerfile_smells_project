FROM sylvainlasnier/ubuntu
MAINTAINER Sylvain Lasnier <sylvain.lasnier@gmail.com>

# Install packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get -y install supervisor apache2 libapache2-mod-php5 mysql-server php5-mysql pwgen php5-mcrypt 

# Add image configuration and scripts
ADD start-apache2.sh /start-apache2.sh
ADD start-mysqld.sh /start-mysqld.sh
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf

#Configure Apache PHP
RUN a2enmod rewrite
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M

# Add volumes 
VOLUME  ["/etc/mysql", "/var/lib/mysql" ]
VOLUME  ["/etc/apache2/sites-enabled","/var/www" ]

EXPOSE 80 3306
CMD ["/run.sh"]
