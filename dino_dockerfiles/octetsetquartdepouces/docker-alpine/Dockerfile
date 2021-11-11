FROM alpine:3.4
MAINTAINER Julien Goret <jgoret@gmail.com>

USER root
# Install usefull binaries
RUN apk update && \
    apk upgrade && \
    apk add sudo && \
    rm -rf /var/cache/apk/* && \
    adduser -S -D -h /home/www-app -s /sbin/nologin -u 1001 www-app && \
    echo "www-app ALL=(ALL) NOPASSWD: apk" >> /etc/sudoers.d/www-app && \
    chmod 0440 /etc/sudoers.d/www-app

ENV HOME /home/www-app
WORKDIR /home/www-app

ONBUILD USER www-app
