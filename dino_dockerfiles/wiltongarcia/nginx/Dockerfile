FROM nginx:alpine

MAINTAINER Wilton Garcia <wiltonog@gmail.com>

RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >> /etc/apk/repositories \
    && apk update \
    && apk add --no-cache --virtual .build-deps shadow \
    && usermod -d /var/www/html -u 1000 nginx \
    && groupmod -g 50 nginx \
    && find / -group 101 -exec chgrp -h nginx {} \; \
    && find / -user 100 -exec chown -h nginx {} \;
