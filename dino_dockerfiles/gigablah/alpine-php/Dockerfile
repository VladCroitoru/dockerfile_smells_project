FROM gigablah/alpine-base:3.2

RUN apk add -U php php-fpm php-json php-ctype php-curl php-openssl nginx ca-certificates \
 && rm -rf /var/cache/apk/*

COPY rootfs /

VOLUME ["/opt/www"]

EXPOSE 80 443
