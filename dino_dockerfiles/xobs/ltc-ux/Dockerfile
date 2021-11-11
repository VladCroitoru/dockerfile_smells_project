FROM nginx:1.11.5-alpine

MAINTAINER Sean Cross <xobs@kosagi.com>

RUN \
    apk add --no-cache --virtual .build-deps \
        curl \
    && \
    curl -SLs -o /build.zip https://github.com/xobs/codebender-test-shell/archive/master.zip && \
    mkdir /build && \
    cd /build && \
    unzip -q /build.zip && \
    rm -f /build.zip && \
    cd * && \
    rm -rf /usr/share/nginx/* && \
    mv html /usr/share/nginx/ && \
    cd / && \
    rm -rf /build && \
    apk del .build-deps

COPY nginx.conf /etc/nginx/conf.d/default.conf