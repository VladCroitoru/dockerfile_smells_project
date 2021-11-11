##################################################################
# Dockerfile automated Docker Hub build - base image for Varnish5
#
# Centos6.8
# Supervisor
# Nginx
# Varnish-5.0.0
#
##################################################################
FROM centos:centos6.8

MAINTAINER sKull99 <jefe99.jeb@gmail.com>

ENV UPDATE "2017-02-10"

## HOSTNAME
RUN echo -e "NETWORKING=yes\nHOSTNAME=centos68-varnish5" > /etc/sysconfig/network

## Add repo nginx
ADD nginx.repo /etc/yum.repos.d/nginx.repo

## Import the Centos6 and add EPEL repo
RUN rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6 \
	&& rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm

## YUM
RUN yum -y install \
	wget \
	nginx \
	supervisor \
	autoconf \
	automake \
	jemalloc-devel \
	libedit-devel \
	libtool \
	ncurses-devel \
	pcre-devel \
	pkgconfig \
	python-docutils \
	python-sphinx \
	graphviz

## VARNISH-5.0.0
RUN wget https://repo.varnish-cache.org/source/varnish-5.0.0.tar.gz -O /usr/local/src/varnish-5.0.0.tar.gz
RUN cd /usr/local/src/ &&  tar xvf varnish-5.0.0.tar.gz
RUN cd /usr/local/src/varnish-5.0.0 && ./autogen.sh
RUN cd /usr/local/src/varnish-5.0.0 && ./configure --prefix=/usr/local/varnish-5.0.0
RUN cd usr/local/src/varnish-5.0.0 && make && make install
RUN ln -s /usr/local/varnish-5.0.0 /usr/local/varnish

## DIRECTORYS
RUN mkdir /etc/varnish
RUN mkdir -p /var/www/default.int
RUN mkdir -p /etc/supervisor/conf.d

## CLEAN UP
RUN rm -rf /usr/local/src/*
RUN rm -rf /etc/nginx/conf.d/*

## NGINX CONF
ADD nginx.conf /etc/nginx/nginx.conf
ADD default.int.conf /etc/nginx/conf.d/default.int.conf
ADD index.html /var/www/default.int/index.html

## VARNISH CONF
ADD default.vcl /etc/varnish/default.vcl

## SUPERVISOR CONF
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

## PORTS
EXPOSE 80 8080

## RUN SUPERVISOR
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
