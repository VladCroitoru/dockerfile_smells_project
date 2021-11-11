FROM ubuntu:trusty

MAINTAINER Amanpreet Singh

ENV OPENRESTY_VERSION 1.9.7.2
ENV BUILD_DEPS libreadline-dev libncurses5-dev libpcre3-dev \
               libssl-dev perl make build-essential curl

# Install OpenResty dependencies
RUN apt-get update && \
    apt-get -y install $BUILD_DEPS && \
    curl -O http://openresty.org/download/ngx_openresty-${OPENRESTY_VERSION}.tar.gz && \
    tar xzvf ngx_openresty-${OPENRESTY_VERSION}.tar.gz && \
    cd /ngx_openresty-${OPENRESTY_VERSION}/  && \
    ./configure --with-luajit \
                --with-http_gzip_static_module \
                --with-http_ssl_module \
                --with-pcre-jit && \
    make && \
    make install && \
    rm -rf /ngx_openresty* && \
    apt-get -y remove $BUILD_DEPS && \
    apt-get -y autoremove

VOLUME ["/opt/nginx"]

EXPOSE 80

CMD ["/usr/local/openresty/nginx/sbin/nginx", "-c", "/opt/nginx/conf/nginx.conf"]
