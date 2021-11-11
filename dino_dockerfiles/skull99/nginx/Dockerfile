########################################################################
# Dockerfile automated Docker Hub build - base image for nginx latest
#
# Centos7
# Nginx
#
########################################################################
FROM centos:latest

MAINTAINER sKull99 <jefe99.jeb@gmail.com>

ENV UPDATE "2017-09-11"

## Install EPEL repo
RUN yum  -y install \
	epel-release

## Install package
RUN yum -y install \
	vim \
	nginx

## DIRECTORYS
RUN mkdir -p /var/www/default.int

## ADD files documentroot
ADD default.int/index.html /var/www/default.int/index.html

## ADD conf nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf

## ADD Conf serverblock
ADD conf.d/default.int.conf /etc/nginx/conf.d/default.int.conf

## PORTS
EXPOSE 80

## CMD
CMD ["nginx", "-g", "daemon off;"]
