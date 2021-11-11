FROM alpine:3.2

EXPOSE 80

RUN echo "@stale http://dl-4.alpinelinux.org/alpine/v3.3/main" >> /etc/apk/repositories && \
    apk add --update nginx-lua@stale \
        lua5.1-cjson@stale && \
    mkdir -p /tmp/nginx/client-body && \
    rm -rf /var/cache/apk/*

COPY . /

CMD ["/usr/sbin/nginx", "-g", "daemon off;", "-p", "/app", "-c", "/nginx.conf"]
