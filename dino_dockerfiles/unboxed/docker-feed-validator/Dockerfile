FROM ubuntu:14.04

MAINTAINER Unboxed Consulting

# Based on http://feedvalidator.org/docs/howto/install_and_run.html
# and https://medium.com/dev-tricks/apache-and-php-on-docker-44faef716150

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install apache2-mpm-worker git python

RUN apt-get clean

RUN rm -rf /var/www
RUN git clone https://github.com/rubys/feedvalidator.git /var/www/

# ADD resource/apache.server.conf /etc/apache2/conf-available/server.conf

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

ADD resources/apache-config.conf /etc/apache2/sites-enabled/000-default.conf

RUN a2enmod cgi rewrite

EXPOSE 80
CMD /usr/sbin/apache2ctl -D FOREGROUND