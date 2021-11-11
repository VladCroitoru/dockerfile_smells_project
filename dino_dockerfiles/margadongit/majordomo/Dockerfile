###############################################
# Dockerfile for Majordomo container to run /md/cycle.php
# Complete set required Apache+PHP7 container and MySQL container
# Based on alpine:3.5
# 17/12/2017
#
FROM alpine:3.5
MAINTAINER margadongit <vpnki.service@gmail.com>

LABEL version="0.1" \
      description="Majordomo image using Linux Alpine 3.5"

###############################################
# Application settings
#
ENV SERVER_NAME="SERVER_NAME"

###############################################
# Install software
#
RUN apk --update add sudo \
    php7 \
    mysql-client \
    php7-mysqli \
    php7-bz2 \
    php7-common \
    php7-curl \
    php7-gd \
    php7-json \
    php7-mbstring \
    php7-mcrypt \
    php7-opcache \
    php7-xml

#############################################
# Setup software in container
#
RUN export SERVER_NAME=SERVER_NAME
RUN export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN ln -s /usr/bin/php7 /usr/bin/php

#############################################
# Expose ports for MQTT,...
#EXPOSE 1883/tcp

CMD ["php", "/md/cycle.php"]
#CMD /bin/ash
