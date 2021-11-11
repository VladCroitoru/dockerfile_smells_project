FROM centos:centos6.6
MAINTAINER Gareth Evans

WORKDIR /srv

RUN yum install -y -q epel-release
RUN yum install -y -q ant
RUN yum install -y -q php php-dom php-pdo php-pecl-apc php-pecl-http1 php-pecl-xdebug php-mcrypt php-mysqli php-mbstring

RUN sed -i 's/short_open_tag = Off/short_open_tag = On/' /etc/php.ini
