FROM php:5.6-alpine
LABEL \
    maintainer="tabiul@gmail.com" \
    description="PHP 5.6 with Apache 2.4 on top of Alpine"


 
# Check latest stable version here: https://suhosin.org/stories/download.html
ENV SUHOSIN_VERSION 0.9.38


RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.3/main' >> /etc/apk/repositories

RUN apk update && \
    apk add ffmpeg-dev=2.8.11-r0 && \
    apk add ffmpeg=2.8.11-r0 && \
    apk add apache2 && \
    apk add apache2-utils && \ 
    apk add php5-apache2 && \
    apk add php5-mysql && \
    apk add php5-mysqli && \
    apk add php5-pear && \
    apk add php5-cgi && \
    apk add php5-curl && \
    apk add php5-dev && \
    apk add php5-fpm && \
    apk add php5-gd && \
    apk add php5-imagick && \
    apk add php5-imap && \
    apk add php5-intl && \
    apk add php5-json && \
    apk add php5-mcrypt && \
    apk add binutils &&\
    apk add git && \
    apk add autoconf && \
    apk add build-base && \
    apk add openssl && \ 
    
    git clone https://github.com/tony2001/ffmpeg-php.git /root/ffmpeg-php && \
    cd /root/ffmpeg-php && \
    phpize && \
    ./configure && \
    make && \
    cp modules/ffmpeg.so /usr/lib/php5/modules/ && \
    echo "extension=ffmpeg.so" > /etc/php5/conf.d/ffmpeg.ini && \
    rm -rf /root/ffmpeg-php && \

    wget https://download.suhosin.org/suhosin-$SUHOSIN_VERSION.tar.gz -P /root && \
    tar xvfz /root/suhosin-$SUHOSIN_VERSION.tar.gz -C /root && \
    cd /root/suhosin-$SUHOSIN_VERSION && \
    # Alpine linux has flock() stuff in file.h
    sed -i '1i#include <sys/file.h>' log.c && \
    phpize && \
    ./configure && \
    make && \
    cp modules/suhosin.so /usr/lib/php5/modules/ && \
    echo "extension=suhosin.so" > /etc/php5/conf.d/suhosin.ini && \
    rm /root/suhosin-$SUHOSIN_VERSION.tar.gz && \
    rm -rf /root/suhosin-$SUHOSIN_VERSION 

    

RUN mkdir -p /run/apache2
EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]

