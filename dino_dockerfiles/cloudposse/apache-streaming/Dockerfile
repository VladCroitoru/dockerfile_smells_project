FROM cloudposse/apache

MAINTAINER Erik Osterman "e@osterman.com"

ENV APACHE_MOD_H264_VERSION 2.2.7

ADD http://h264.code-shop.com/download/apache_mod_h264_streaming-${APACHE_MOD_H264_VERSION}.tar.gz /usr/src/apache_mod_h264_streaming.tar.gz
ADD http://people.apache.org/~pquerna/modules/mod_flvx.c /usr/src/mod_flvx.c

RUN apt-get update && \
    apt-get -y install apache2-threaded-dev build-essential && \
    tar -zvxf /usr/src/apache_mod_h264_streaming.tar.gz -C /usr/src/ &&  \
    cd /usr/src/mod_h264_streaming-${APACHE_MOD_H264_VERSION}/ && \
    ./configure --with-apxs=`which apxs` && \
    make && \
    make install && \
    apxs2 -c -i /usr/src/mod_flvx.c && \
    chmod 644 /usr/lib/apache2/modules/mod_flvx.so && \
    apt-get -y remove build-essential && \
    dpkg --get-selections | awk '{print $1}'|cut -d: -f1|grep -- '-dev$' | xargs apt-get remove -y && \
    rm -rf /usr/src && \
    apt-get clean all && \
    rm -rf /tmp/*

ADD mods-available/ /etc/apache2/mods-available/

RUN a2enmod h264_streaming && \
    a2enmod flvx

