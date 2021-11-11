FROM liyyt/openresty:latest
MAINTAINER Aaron Bolanos <aaron@liyyt.com>

COPY config/nginx.conf /usr/local/openresty/nginx/conf/nginx.conf
COPY config/conf.d/default.conf /usr/local/openresty/nginx/conf/conf.d/default.conf

ENTRYPOINT ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]