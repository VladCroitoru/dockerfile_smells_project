FROM       ubuntu:14.04
MAINTAINER Yefry Figueroa "https://github.com/yefryf/webserver"

# Set to no tty
ENV DEBIAN_FRONTEND noninteractive

# nginx + php-fpm
RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y software-properties-common && \
    nginx=stable && \
    add-apt-repository ppa:nginx/$nginx && \
    apt-get update && \
    BUILD_PACKAGES="supervisor nginx php5-fpm git php5-mysql php5-curl php5-gd php5-intl php5-mcrypt php5-memcache php5-sqlite php5-xmlrpc php5-xsl pwgen" && \
    apt-get -y install $BUILD_PACKAGES && \
    apt-get remove --purge -y software-properties-common && \
    apt-get autoremove -y && apt-get clean && apt-get autoclean

# OpenSSH
RUN apt-get install -y openssh-server vim

RUN echo 'root:toor' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# MariaDB 5.5
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db && \
    echo 'deb http://mirrors.syringanetworks.net/mariadb/repo/5.5/ubuntu trusty main' >> /etc/apt/sources.list && \
    echo 'deb-src http://mirrors.syringanetworks.net/mariadb/repo/5.5/ubuntu trusty main' >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y mariadb-server pwgen && \
    rm -rf /var/lib/mysql/* && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

## install_db to fix issue not starting
RUN mysql_install_db --user=mysql --ldata=/var/lib/mysql/ && \
    echo "export TERM=dumb" >> ~/.bashrc

## root privilegde mysql
ENV MYSQL_USER=admin \
    MYSQL_PASS=**Random**

# Needed dirs
RUN mkdir /var/run/sshd && \
    mkdir /var/run/supervisor && \
    mkdir -p /var/log/supervisor

ADD nginx-vhost.conf /etc/nginx/sites-available/default
ADD index.php /var/www/html/index.php
COPY createdbsuer.sh /tmp/createdbsuer.sh

RUN chmod 700 /tmp/*

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 22 80 3306

CMD ["/usr/bin/supervisord"]
