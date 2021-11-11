FROM ubuntu:14.04.2

MAINTAINER Alexander Miehe <alexander.miehe@gmail.com>
ENV NGINX_VERSION 1.7.12

RUN apt-get update \
    && apt-get install -y curl gcc libpcre3-dev libssl-dev make \
    && mkdir -p /tmp/nginx \
    && cd /tmp/nginx \
    && curl -O http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \
    && tar -zxvf nginx-${NGINX_VERSION}.tar.gz \
    && rm -f nginx-${NGINX_VERSION}.tar.gz \
    && mkdir -p /opt/nginx \
    && cd /tmp/nginx/nginx-${NGINX_VERSION} \
    && ./configure --with-ipv6 --with-http_stub_status_module --with-http_ssl_module --with-http_spdy_module --prefix=/opt/nginx \
    && make \
    && make install \
    && rm -rf /tmp/nginx \
    && apt-get remove -y gcc make \
    && apt-get -y autoremove

CMD ["/opt/nginx/sbin/nginx"]
