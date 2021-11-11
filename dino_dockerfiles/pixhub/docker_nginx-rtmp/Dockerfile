FROM alpine:3.7

ENV NGINX_VERSION=1.13.7 \
    STREAM_HOST=localhost \
    PROTO=http

RUN apk update && \
    apk add \
        build-base \
        zlib-dev \
        pcre-dev \
        openssl-dev \
        wget \
        git && \
    mkdir /HLS && \
    mkdir /HLS/live && \
    mkdir /video_recordings && \
    cd /tmp && \
    git clone git://github.com/arut/nginx-rtmp-module.git && \
    wget http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz && \
    tar xzvf nginx-$NGINX_VERSION.tar.gz && \
    cd /tmp/nginx-$NGINX_VERSION && \
    ./configure \
        --add-module=../nginx-rtmp-module \
        --prefix=/usr/local/nginx \
        --conf-path=/usr/local/nginx/conf/nginx.conf \
        --sbin-path=/usr/local/sbin/nginx \
        --pid-path=/run/nginx.pid && \
    make && \
    make install && \
    cd / && \
    rm -rf /tmp/* && \
    apk del \
        git \
        build-base \
        wget

COPY files /

CMD ["/run.sh"]
