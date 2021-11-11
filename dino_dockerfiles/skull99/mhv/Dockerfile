########################################################################
# Dockerfile automated Docker Hub build - base image for SSL Terminator
#
# Centos6.8
# Supervisor
# Haproxy
# Varnish 4
#
########################################################################
FROM centos:centos6.8

MAINTAINER sKull99 <jefe99.jeb@gmail.com>

ENV UPDATE "2017-02-21"

## HOSTNAME
RUN echo -e "NETWORKING=yes\nHOSTNAME=centos68Balancer" > /etc/sysconfig/network

## Add repo varnish4
RUN rpm -Uvh http://repo.varnish-cache.org/redhat/varnish-4.0/el6/noarch/varnish-release/varnish-release-4.0-4.el6.noarch.rpm

## Import the Centos6 and add EPEL repo
RUN rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6 \
	&& rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm

## YUM
RUN yum -y install \
	wget \
	varnish \
	haproxy \
	supervisor

## DIRECTORYS
RUN mkdir -p /etc/supervisor/conf.d

## HAPROXY CONF
ADD haproxy.cfg /etc/haproxy/haproxy.cfg

## VARNISH CONF
ADD default.vcl /etc/varnish/default.vcl

## SUPERVISOR CONF
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

## PORTS
EXPOSE 80 8080

## RUN SUPERVISOR
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
