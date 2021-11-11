FROM php:7.0.13-fpm-alpine

MAINTAINER Sean Cross <xobs@kosagi.com>

RUN apk update && \
    apk add --no-cache --virtual .build-deps \
        curl \
    && \
    curl -SLs -o /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && \
    curl -SLs -O https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-2.23-r3.apk && \
    apk add glibc-2.23-r3.apk && \
    rm -f glibc-2.23-r3.apk && \
    mkdir -p /opt/codebender/ && \
    curl -SLs -o /v167.zip https://github.com/xobs/arduino-compiler/archive/v167.zip && \
    unzip -q -d /opt/codebender /v167.zip && \
    rm -f /v167.zip && \
    mv /opt/codebender/* /opt/codebender/codebender-arduino-core-files && \
    chmod -R a+x /opt/codebender && \
    apk del .build-deps && \
    mkdir -p /var/cache/filebkp

COPY app.php /