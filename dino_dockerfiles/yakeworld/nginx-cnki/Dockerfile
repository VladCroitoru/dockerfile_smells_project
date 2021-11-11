FROM debian:stretch-slim
MAINTAINER yakeworld@gmail.com 
RUN apt update \
    && apt-get -yq install build-essential wget git \
    && mkdir /var/nginx \
    && wget -qO- http://nginx.org/download/nginx-1.15.2.tar.gz | tar xz -C /var/nginx/  \
    && wget -qO-  ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.42.tar.gz | tar xz -C /var/nginx/  \
    && wget --no-check-certificate  -qO-  https://www.openssl.org/source/openssl-1.0.2p.tar.gz | tar xz -C /var/nginx/ \
    && wget -qO-  http://www.zlib.net/zlib-1.2.11.tar.gz | tar xz -C /var/nginx/  \
    && git clone git://github.com/yaoweibin/ngx_http_substitutions_filter_module.git /var/nginx/ngx_http_substitutions_filter_module/ \
    && cd /var/nginx/pcre-8.42 \
    && ./configure \
    && make \
    && make install \
    && cd /var/nginx/zlib-1.2.11 \
    && ./configure \
    && make \
    && make install \
    && cd /var/nginx/openssl-1.0.2p \
    && ./config \
    && make \
    && make install \
    && cd /var/nginx/nginx-1.15.2 \
    && ./configure --user=www --group=www --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module --with-http_gzip_static_module --with-ipv6 --with-http_sub_module --add-module=/var/nginx/ngx_http_substitutions_filter_module  --with-openssl=/var/nginx/openssl-1.0.2p   --with-zlib=/var/nginx/zlib-1.2.11 \
    && make \
    && make install \
    && cd / \
    && rm -r /var/nginx \
    && useradd -s /sbin/nologin -M www \
    && mkdir -p /usr/local/nginx/external \
    && mkdir -p /usr/local/nginx/conf.d \
    #&& wget --no-check-certificate https://raw.githubusercontent.com/yakeworld/nginx-cnki/master/basic.conf -O /usr/local/nginx/conf.d/basic.conf \
    && wget --no-check-certificate https://raw.githubusercontent.com/yakeworld/nginx-cnki/master/ssl.conf -O /usr/local/nginx/conf.d/ssl.conf \
    && wget --no-check-certificate https://raw.githubusercontent.com/yakeworld/nginx-cnki/master/nginx.conf -O /usr/local/nginx/conf/nginx.conf \
    && wget --no-check-certificate https://raw.githubusercontent.com/yakeworld/nginx-cnki/master/vhost_proxy.conf -O /usr/local/nginx/conf.d/vhost_proxy.conf \
    && wget --no-check-certificate https://raw.githubusercontent.com/yakeworld/nginx-cnki/master/entrypoint.sh -O /opt/entrypoint.sh \
    && chmod a+x /opt/entrypoint.sh
#ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["/usr/local/nginx/sbin/nginx"]    