FROM alpine

RUN apk update
RUN apk add --update ffmpeg
RUN apk add --update make gcc musl-dev pcre-dev openssl-dev zlib-dev \
ncurses-dev readline-dev curl perl wget git
RUN rm -rf /var/cache/apk/*

RUN addgroup nginx
RUN adduser -S -G nginx nginx

RUN cd /root && git clone https://github.com/arut/nginx-rtmp-module.git

ENV OPENRESTY_VERSION 1.9.3.1
RUN wget -nv http://openresty.org/download/ngx_openresty-$OPENRESTY_VERSION.tar.gz \
         -O /root/ngx_openresty-$OPENRESTY_VERSION.tar.gz \
 && tar -xzf /root/ngx_openresty-$OPENRESTY_VERSION.tar.gz -C /root/ \
 && cd /root/ngx_openresty-$OPENRESTY_VERSION/ \
 && ./configure \
    --prefix=/usr/local/openresty \
    --with-http_gunzip_module \
    --with-luajit \
    --with-luajit-xcflags=-DLUAJIT_ENABLE_CHECKHOOK \
    --http-client-body-temp-path=/var/nginx/client_body_temp \
    --http-proxy-temp-path=/var/nginx/proxy_temp \
    --http-log-path=/var/nginx/access.log \
    --error-log-path=/var/nginx/error.log \
    --pid-path=/var/nginx/nginx.pid \
    --lock-path=/var/nginx/nginx.lock \
    --with-http_stub_status_module \
    --with-http_ssl_module \
    --with-http_realip_module \
    --without-http_fastcgi_module \
    --without-http_uwsgi_module \
    --without-http_scgi_module \
    --add-module=/root/nginx-rtmp-module --user=nginx \
    && make \
    && make install

RUN mkdir -p /var/log/nginx \
             /usr/local/openresty/nginx/conf/server_conf \
             /usr/local/openresty/nginx/conf/rtmp_conf \
             /usr/local/openresty/nginx/conf/lua


ADD nginx.conf.template /usr/local/openresty/nginx/conf/nginx.conf.template
ADD appinit /usr/bin/appinit
RUN chmod 744 /usr/bin/appinit

EXPOSE 80
EXPOSE 1935
EXPOSE 6379

CMD ["appinit"]
