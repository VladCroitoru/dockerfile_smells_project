FROM alpine:3.2

RUN set -x; apk add -U tar gcc wget build-base openssl perl pcre-dev openssl-dev ca-certificates; \
  wget https://openresty.org/download/openresty-1.9.7.4.tar.gz; \
  tar -xzf openresty-1.9.7.4.tar.gz; \
  cd openresty-1.9.7.4; \
  ./configure --with-luajit; \
  make && make install; \
  cd ..; rm -Rf openresty-1.9.7.4; rm openresty-1.9.7.4.tar.gz; \
  apk del tar gcc wget build-base perl pcre-dev openssl-dev openssl

# Default Environment
ENV NGINX_LOG /data/log/nginx.log
ENV NGINX_LOG_LEVEL info
ENV NGINX_ACCESS_LOG /data/log/nginx_access.log
ENV NGINX_ACCESS_LOG_FORMAT forwarded

RUN apk add -U pcre libpcre32 libgcc

ADD scripts /etc/nginx/scripts
ADD nginx.conf /etc/nginx/nginx.conf

VOLUME /data

CMD /usr/local/openresty/nginx/sbin/nginx -c /etc/nginx/nginx.conf
