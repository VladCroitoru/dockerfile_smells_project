FROM debian:latest
MAINTAINER Curtis Baldwinson <curtisbaldwinson@gmail.com>

# Apache2
RUN apt-get update && apt-get -y install apache2 && apt-get clean
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

# PHP5, APC, some useful stuff etc...
RUN apt-get -y install git php5-dev libpcre3-dev gcc make php5-mysql libapache2-mod-php5 curl php5-curl php-apc

# Enable mass dynamic virtual hosts
RUN a2enmod rewrite
RUN a2dissite 000-default
RUN a2enmod vhost_alias
ADD ./catchall /etc/apache2/sites-available/catchall
RUN a2ensite catchall

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
