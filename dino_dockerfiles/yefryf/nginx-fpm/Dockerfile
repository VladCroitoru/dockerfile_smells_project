FROM       ubuntu:14.04
MAINTAINER Yefry Figueroa

# Set to no tty
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y software-properties-common && \
    LANG=C.UTF-8 add-apt-repository ppa:ondrej/php && \
    nginx=stable && \
    add-apt-repository ppa:nginx/$nginx && \
    apt-get update && \
    BUILD_PACKAGES="supervisor nginx php5.6-fpm git php5.6-mysql php5.6-cli php5.6-json php5.6-curl php5.6-gd php5.6-intl php5.6-mcrypt php5.6-memcache php5.6-sqlite php5.6-xmlrpc php5.6-xsl pwgen" && \
    apt-get -y install $BUILD_PACKAGES && \
    apt-get remove --purge -y software-properties-common && \
    apt-get autoremove -y && apt-get clean && apt-get autoclean

# OpenSSH
RUN apt-get install -y openssh-server vim

RUN echo 'root:toor' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# Needed dirs
RUN mkdir /var/run/sshd && \
    mkdir /var/run/supervisor && \
    mkdir -p /var/log/supervisor && \
    mkdir /run/php

ADD nginx-vhost.conf /etc/nginx/sites-available/default
ADD index.php /var/www/html/index.php

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 22 80

CMD ["/usr/bin/supervisord"]
