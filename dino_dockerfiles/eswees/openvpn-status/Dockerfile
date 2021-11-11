FROM centos:latest

MAINTAINER Yuriy Golik <eswees@pyhead.net>

EXPOSE  80

## Переопределяем каталог
WORKDIR /var/www/html

## Ставим Web Server и всё остальное
RUN yum install -y epel-release && yum update -y && yum install -y \
        python-GeoIP \
        python-ipaddr \
        python-humanize \
        python-bottle \
        python-semantic_version \
        httpd \
        mod_wsgi \
        git \
        wget \
	&& yum clean all

RUN git clone https://github.com/furlongm/openvpn-monitor.git /var/www/html

COPY ./httpd.conf /etc/httpd/conf/httpd.conf

CMD \
  wget -N http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz \
  && gunzip GeoLiteCity.dat.gz \
  && mv GeoLiteCity.dat /usr/share/GeoIP/GeoIPCity.dat \
  && rm -rf /run/httpd/* \
  && /usr/sbin/apachectl -DFOREGROUND

