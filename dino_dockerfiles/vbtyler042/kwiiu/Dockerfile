FROM ubuntu:15.10

MAINTAINER VbTyler042 <vbtyler042@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN echo "deb http://archive.ubuntu.com/ubuntu wily main universe" > /etc/apt/sources.list && \
    apt-get update && \
    apt-get -y install nginx \
    curl \
    wget \
    supervisor \
    php5 \
    php5-fpm \
    --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

ADD asset/* /opt/

RUN sed -i '/daemonize /c \daemonize = no' /etc/php5/fpm/php-fpm.conf && \
    sed -i '/;cgi.fix_pathinfo/c \cgi.fix_pathinfo=0' /etc/php5/fpm/php.ini && \
    cp -f /opt/default /etc/nginx/sites-available/default && \
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
    mkdir /site && \
    chown www-data:www-data /site

ADD site /site

EXPOSE 80 443

CMD /usr/bin/supervisord -c /opt/supervisord.conf
