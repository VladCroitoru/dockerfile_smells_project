FROM debian:jessie

LABEL maintainer "João Miguel <joao@miguel.ms>"
LABEL repository="https://github.com/jmtvms/ngx_pagespeed.git"
LABEL bugs="https://github.com/jmtvms/ngx_pagespeed/issues"
LABEL github="https://github.com/jmtvms/ngx_pagespeed"
LABEL version="1.0.1"

RUN apt-get -y update && apt-get install -y \
    wget \
    build-essential \
    libpcre3-dev \
    zlib1g-dev

ENV NGINX_VERSION=1.11.12
ENV NPS_VERSION=1.11.33.4-beta
ENV PSOL_VERSION=1.11.33.4
ENV SUBS_VERSION=0.6.4
ENV OPENSSL_VERSION=1.1.0e

RUN useradd -r -s /usr/sbin/nologin nginx

RUN ["mkdir","/usr/nginx_source/"]
WORKDIR "/usr/nginx_source/"

# Preparing Nginx
RUN wget -qO nginx.tar.gz http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz
RUN tar -xvzf nginx.tar.gz

# Preparing ngx_http_substitutions_filter_module
RUN wget -qO ngx_http_substitutions_filter_module.tar.gz https://github.com/yaoweibin/ngx_http_substitutions_filter_module/archive/v$SUBS_VERSION.tar.gz
RUN tar -xzvf ngx_http_substitutions_filter_module.tar.gz

# Preparing OpenSSL
RUN wget -qO openssl.tar.gz https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz
RUN tar -xvzf openssl.tar.gz
RUN ls

# Preparing PageSpeed
RUN wget -O ngpagespeed.tar.gz https://github.com/apache/incubator-pagespeed-ngx/archive/v$NPS_VERSION.tar.gz
RUN tar -xvzf ngpagespeed.tar.gz
WORKDIR "/usr/nginx_source/incubator-pagespeed-ngx-$NPS_VERSION/"
RUN wget https://dl.google.com/dl/page-speed/psol/$PSOL_VERSION.tar.gz
RUN tar -xzvf $PSOL_VERSION.tar.gz

# Building Nginx
WORKDIR "/usr/nginx_source/nginx-$NGINX_VERSION/"

RUN ./configure \
    --add-module=/usr/nginx_source/incubator-pagespeed-ngx-$NPS_VERSION \
    --add-module=/usr/nginx_source/ngx_http_substitutions_filter_module-$SUBS_VERSION \
    --with-openssl=/usr/nginx_source/openssl-$OPENSSL_VERSION \
    --with-http_ssl_module  \
    --user=nginx  \
    --group=nginx \
    --prefix=/opt/nginx \
    --sbin-path=/opt/nginx/nginx \
    --pid-path=/var/nginx/nginx.pid \
    --error-log-path=/var/nginx/logs/error.log \
    --http-log-path=/var/nginx/logs/access.log \
    --conf-path=/opt/nginx/conf/nginx.conf


RUN make
RUN make install

RUN rm -rfd /usr/nginx_source

RUN apt-get purge -y \
    wget \
    build-essential \
    libpcre3-dev \
    zlib1g-dev \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV NGX_LOGLEVEL=debug
ENV NGX_UPSTREAM_NAME=www.google.com
ENV NGX_UPSTREAM_SERVER=www.google.com:80

ENV NPS_ENABLED=on

COPY content/nginx.conf /opt/nginx/conf/
COPY content/robots.txt /opt/nginx/html/

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/nginx/logs/access.log
RUN ln -sf /dev/stderr /var/nginx/logs/error.log

WORKDIR /opt/nginx/
COPY start.sh ./
RUN chmod +x start.sh

ENTRYPOINT ["./start.sh"]
CMD ["-g", "'daemon off;'"]

EXPOSE 80
EXPOSE 443

VOLUME ["/opt/nginx/conf/"]
VOLUME ["/opt/nginx/html/"]
VOLUME ["/var/nginx/logs/"]