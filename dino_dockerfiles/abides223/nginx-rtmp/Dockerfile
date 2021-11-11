# Dockerizing nginx-RTMP: Dockerfile for building nginx-RTMP images
# Based on ubuntu:latest, installs nginx-RTMP

# Format: FROM    repository[:version]
FROM       ubuntu:latest

# Format: MAINTAINER Name <email@addr.ess>
MAINTAINER Andreas W. Prang <writeAmail@me.com>
MAINTAINER Kelvin D. Klein <gamemasterkleinish@gmail.com>

# VARIABLES
ENV nginxVersion nginx-1.9.2

# Installation:
RUN apt-get update;\
        apt-get -y install wget;\
        apt-get -y install unzip;\
        apt-get install -y build-essential libpcre3 libpcre3-dev libssl-dev

# Install nginx with RTMP
RUN mkdir /tmp/working && cd /tmp/working;\
        wget http://nginx.org/download/${nginxVersion}.tar.gz;\
        wget https://github.com/arut/nginx-rtmp-module/archive/master.zip;\
        tar -zxvf ${nginxVersion}.tar.gz;\
        unzip master.zip;\
        cd ${nginxVersion};\
        ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module-master --with-debug;\
        make install clean

RUN rm -r /tmp/working

# Install daemon
RUN wget https://raw.github.com/JasonGiedymin/nginx-init-ubuntu/master/nginx -O /etc/init.d/nginx;\
        chmod +x /etc/init.d/nginx;\
        update-rc.d nginx defaults

# Install additional decoder
#RUN apt-get -y install software-properties-common;\
#        apt-add-repository ppa:jon-severinsson/ffmpeg;\
#        apt-get update;\
#        apt-get -y install ffmpeg

RUN apt-add-repository ppa:samrog131/ppa; \
         apt-get update; \
         apt-get install FFmpeg-real; \
         ln -sf /opt/FFmpeg/bin/FFmpeg /usr/bin/FFmpeg

# Expose HTTP & RTMP
EXPOSE 80
EXPOSE 1935

ADD nginx.conf /usr/local/nginx/conf/nginx.conf
RUN rm /usr/local/nginx/conf/mime.types
ADD mime.types /usr/local/nginx/conf/mime.types

RUN mkdir -p /var/log/nginx/
RUN ln -s /usr/local/nginx/html /var/www
RUN mkdir -p /var/www/HLS/
ADD stat.xsl /var/www/HLS/stat.xsl
ADD html/* /var/www/

## run as daemon
# Run
CMD service nginx start

## run interactive
#  CMD service nginx start & /bin/bash

# Clean // TODO: NOT WORKING
# RUN apt-get -y purge wget unzip build-essential libpcre3 libpcre3-dev libssl-dev software-properties-common




