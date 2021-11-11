# docker build -t jerrybendy/nginx-http2 .

FROM debian:jessie

MAINTAINER Jerry Bendy <jerry@icewingcc.com>


RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
            build-essential libpcre3 libpcre3-dev zlib1g-dev unzip git

# add verndor files
COPY vendors/nginx-ct-1.3.2.zip /usr/local/src/nginx-ct.zip
COPY vendors/openssl-OpenSSL_1_0_2j.tar.gz /usr/local/src/openssl.tar.gz
COPY vendors/nginx-1.11.8.tar.gz /usr/local/src/nginx.tar.gz

# unzip all vendor files
RUN cd /usr/local/src \
    && unzip nginx-ct.zip \
    && mv nginx-ct-1.3.2/ nginx-ct \
    && tar zxf openssl.tar.gz \
    && mv openssl-OpenSSL_1_0_2j/ openssl \
    && tar zxf nginx.tar.gz \
    && mv nginx-1.11.8/ nginx

# compile and install 
RUN cd /usr/local/src/nginx \
    && ./configure \
            --add-module=../nginx-ct \
            --with-openssl=../openssl \
            --with-http_v2_module \
            --with-http_ssl_module \
            --with-http_gzip_static_module \
            --with-http_stub_status_module \
    && make \
    && make install
    
# clean
RUN rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/local/src/* 

# forward request and error logs to docker log collector
RUN mkdir -p /var/log/nginx \ 
    && touch /var/log/nginx/access.log \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && touch /var/log/nginx/error.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log


# add default nginx conf files
ADD nginx.conf /usr/local/nginx/conf/nginx.conf

EXPOSE 80 443

CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]