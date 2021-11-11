FROM ubuntu
MAINTAINER William Bouzane <williambouzane@gmail.com>

RUN apt-get update 

RUN apt-get -y upgrade

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install libapache2-mod-php5 php5-cli php5-mysql php5-gd php5-snmp php-pear snmp graphviz php5-mcrypt php5-json subversion mysql-server mysql-client rrdtool fping imagemagick whois mtr-tiny nmap ipmitool python-mysqldb wget

RUN mkdir -p /opt/observium

WORKDIR /opt

RUN wget http://www.observium.org/observium-community-latest.tar.gz

RUN tar zxvf observium-community-latest.tar.gz

RUN rm /opt/observium-community-latest.tar.gz

WORKDIR /opt/observium

RUN cp config.php.default config.php

RUN mkdir logs

RUN mkdir rrd

RUN chown www-data:www-data rrd

