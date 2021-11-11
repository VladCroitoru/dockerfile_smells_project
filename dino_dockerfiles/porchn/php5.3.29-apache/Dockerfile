FROM ubuntu:12.04
#MAINTAINER Ke Ma <ke.ma@wearesuburb.com>

RUN apt-get update && \ 
apt-get install -y curl wget


# Dotdeb mirrors
RUN     wget -qO /root/dotdeb.gpg http://www.dotdeb.org/dotdeb.gpg
RUN     apt-key add /root/dotdeb.gpg 
RUN     echo "deb http://dotdeb.netmirror.org/ squeeze all" > /etc/apt/sources.list.d/dotdeb.list
RUN     echo "deb-src http://dotdeb.netmirror.org/ squeeze all" >> /etc/apt/sources.list.d/dotdeb.list
RUN     apt-get update

# Apache
RUN     apt-get -y install apache2 libapache2-mod-php5
RUN     a2enmod rewrite
RUN     a2enmod headers
ENV         APACHE_RUN_USER www-data
ENV         APACHE_RUN_GROUP www-data
ENV         APACHE_LOG_DIR /var/log/apache2
RUN         rm /var/www/index.html
RUN         chown -R www-data:www-data /var/www
#ADD         conf/apache/default /etc/apache2/sites-available/default
#RUN         sed -i 's/export APACHE_LOG_DIR=\/var\/log\/apache2$SUFFIX/export APACHE_LOG_DIR=\/var\/www\/logs\/apache2$SUFFIX/g' /etc/apache2/envvars
ENV APACHE_LOCK_DIR=/var/lock/apache2
ENV APACHE_PID_FILE=/var/run/apache2/apache2.pid
ENV APACHE_RUN_DIR=/var/run/apache2/
ENV APACHE_RUN_USER=www-data
ENV APACHE_RUN_GROUP=www-data
ENV APACHE_LOG_DIR=/var/log/apache2
RUN     usermod -u 1002 www-data

# PHP
RUN apt-get update && \
apt-get dist-upgrade -y && \
apt-get -y install php5-cli php5-curl php-soap php5-gd php5-mcrypt php5-mysql php5-xmlrpc php5-xsl


RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
WORKDIR /var/www/

EXPOSE 80
EXPOSE 443

VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2/sites-enabled"]

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

