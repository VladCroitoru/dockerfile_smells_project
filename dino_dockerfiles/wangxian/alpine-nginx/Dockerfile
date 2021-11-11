FROM alpine:latest
MAINTAINER WangXian <xian366@126.com>

ENV NGINX_VERSION nginx-1.8.0

RUN apk --update add openssl-dev pcre-dev zlib-dev wget build-base && \
    mkdir -p /tmp/src && \
    cd /tmp/src && \
    wget http://nginx.org/download/${NGINX_VERSION}.tar.gz && \
    tar -zxvf ${NGINX_VERSION}.tar.gz && \
    wget http://labs.frickle.com/files/ngx_cache_purge-2.3.tar.gz && \
    tar -zxvf ngx_cache_purge-2.3.tar.gz && \
    cd /tmp/src/${NGINX_VERSION} && \
    ./configure \
        --with-http_ssl_module \
        --with-http_gzip_static_module \
        --prefix=/etc/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --http-log-path=/app/logs/access.log \
        --error-log-path=/app/logs/error.log \
        --sbin-path=/usr/local/sbin/nginx \
        --add-module=/tmp/src/ngx_cache_purge-2.3 \
        --with-http_sub_module && \
    make && \
    make install && \
    apk del build-base && \
    rm -rf /tmp/src && \
    rm -rf /var/cache/apk/*


WORKDIR /app
VOLUME /app

ADD . .
ADD conf/nginx.conf /etc/nginx/
ADD startup.sh /startup.sh

RUN mkdir -p /app/logs

EXPOSE 80 443
CMD ["/startup.sh"]
