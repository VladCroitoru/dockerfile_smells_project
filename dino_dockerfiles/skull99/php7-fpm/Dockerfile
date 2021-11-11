########################################################################
# Dockerfile automated Docker Hub build - base image for PHP7
#
# Centos7
# PHP7
#
########################################################################
FROM centos:latest

MAINTAINER sKull99 <jefe99.jeb@gmail.com>

ENV UPDATE "2017-09-12"

## Install EPEL repo
RUN yum  -y install \
        epel-release

## WEBTATIC repo
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

## Install PHP7
RUN yum -y install \
	php70w.x86_64 \
	php70w-gd.x86_64 \
	php70w-cli.x86_64 \
	php70w-fpm.x86_64 \
	php70w-pear.noarch \
	php70w-mysql.x86_64 \
	php70w-devel.x86_64 \
	php70w-common.x86_64 \
	php70w-mcrypt.x86_64 \
	php70w-opcache.x86_64 \
	php70w-mbstring.x86_64

## CLEAN YUM
RUN yum -y clean all

## ADD conf FPM
ADD php.conf/php.ini /etc/php.ini
ADD php.conf/php-fpm.conf /etc/php-fpm.conf
ADD php.conf/www.conf /etc/php-fpm.d/www.conf

## PORTS
EXPOSE 9000

CMD ["/usr/sbin/php-fpm", "-F", "-R"]
