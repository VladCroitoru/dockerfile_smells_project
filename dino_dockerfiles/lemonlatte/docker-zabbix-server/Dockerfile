FROM ubuntu:14.04

MAINTAINER Jim Yeh <jimyeh@vm5.com>

RUN apt-get -qq update
RUN apt-get -yqq install supervisor
RUN apt-get -yqq install mysql-client php5-mysql zabbix-server-mysql zabbix-frontend-php

# Zabbix configuration file manipulation
RUN sed -i -e 's/^post_max_size =.*/post_max_size = 16M/' -e 's/^max_execution_time.*/max_execution_time = 300/' \
           -e 's/^max_input_time.*/max_input_time = 300/' -e 's/;date.timezone.*/date.timezone = Asia\/Taipei/' /etc/php5/apache2/php.ini

RUN cp /usr/share/doc/zabbix-frontend-php/examples/apache.conf /etc/apache2/conf-available/zabbix.conf
RUN ln -s /etc/apache2/conf-available/zabbix.conf /etc/apache2/conf-enabled/zabbix.conf

RUN sed -i s/START=no/START=yes/g /etc/default/zabbix-server
RUN mkdir -p /var/run/zabbix
RUN chown zabbix:zabbix /var/run/zabbix

ADD zabbix-initdb.sh /
ADD bootstrap.sh /
ADD zabbix.super.conf /etc/supervisor/conf.d/zabbix.conf

CMD ["/bootstrap.sh"]

