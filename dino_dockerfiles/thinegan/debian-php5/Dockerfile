FROM debian:jessie
MAINTAINER Thinegan Ratnams <thinegan@thinegan.com>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y locales supervisor
RUN apt-get install -y php5-mysql php5-xmlrpc php5-readline php5-ldap php5-json php5-imagick \
php5-gd php5-dev php5-curl php5-cli php5-mcrypt php5-fpm

ADD config/custom.ini /etc/php5/conf.d/custom.ini
ADD supervisord.conf /etc/supervisor/supervisord.conf
ADD supervisor-config/php.sv.conf /etc/supervisor/conf.d/

EXPOSE 9000
# Define default command
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]
