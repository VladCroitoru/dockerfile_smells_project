FROM ubuntu:14.04
MAINTAINER yumin9822 <yumin9822@gmail.com>
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
wget libpcre3 libpcre3-dev zlib1g-dev libssl-dev build-essential git \
&& apt-get clean

RUN mkdir -p /nginx \
    && mkdir -p /var/tmp/nginx \
    && mkdir -p /etc/nginx/sites-enabled \
    && mkdir -p /var/log/nginx \
    && mkdir -p /var/cache/nginx/cache \
    && mkdir -p /var/cache/nginx/temp \
    && mkdir -p /ssl

RUN cd /nginx \
    && wget http://nginx.org/download/nginx-1.8.0.tar.gz \
    && tar zxvf nginx-1.8.0.tar.gz \
    && git clone https://github.com/cuber/ngx_http_google_filter_module \
    && git clone https://github.com/yaoweibin/ngx_http_substitutions_filter_module

RUN cd /nginx/nginx-1.8.0/; ./configure \
    --prefix=/usr --conf-path=/etc/nginx/nginx.conf --pid-path=/var/run/nginx.pid \
    --lock-path=/var/lock/nginx.lock --http-client-body-temp-path=/var/tmp/nginx/client \
    --http-proxy-temp-path=/var/tmp/nginx/proxy --http-fastcgi-temp-path=/var/tmp/nginx/fastcgi \
    --http-scgi-temp-path=/var/tmp/nginx/scgi --http-uwsgi-temp-path=/var/tmp/nginx/uwsgi \
    --with-http_ssl_module --with-http_gzip_static_module --with-ipv6 --with-http_sub_module \
    --add-module=/nginx/ngx_http_google_filter_module \
    --add-module=/nginx/ngx_http_substitutions_filter_module; make; make install; rm -rf /nginx

ADD nginx /etc/init.d/nginx
RUN chmod +x /etc/init.d/nginx; update-rc.d nginx defaults

RUN rm /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
ADD google.conf /etc/nginx/sites-enabled/google.conf
ADD server.crt /ssl/server.crt
ADD server.key /ssl/server.key

VOLUME /var/log/nginx

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
