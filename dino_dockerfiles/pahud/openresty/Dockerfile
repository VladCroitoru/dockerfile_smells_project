FROM debian:jessie
#FROM ubuntu:trusty

MAINTAINER Pahud Hsieh <pahudnet@gmail.com>

ENV \
  DEBIAN_FRONTEND=noninteractive \
  TERM=xterm-color

# Docker Build Arguments
ARG version="1.13.6.1"
ENV orbase /usr/local/openresty

#ADD sources.list.tw /etc/apt/sources.list

RUN apt-get update && apt-get -y upgrade && apt-get -y install --no-install-recommends \
  unzip \
  ca-certificates \
  build-essential \
  vim-tiny \
  curl \
  telnet \
  libreadline-dev \
  libncurses5-dev \
  libpcre3-dev \
  libssl-dev \
  nano \
  perl \
  wget \
  supervisor

# Compile openresty from source.
RUN \
  wget https://openresty.org/download/openresty-${version}.tar.gz && \
  tar -xzvf openresty-*.tar.gz && \
  rm -f openresty-*.tar.gz && \
  cd openresty-* && \
  sed -ie 's/DEFAULT_ENCODE_EMPTY_TABLE_AS_OBJECT 1/DEFAULT_ENCODE_EMPTY_TABLE_AS_OBJECT 0/g' bundle/lua-cjson-*/lua_cjson.c && \
  ./configure \
  --prefix=/opt/openresty \
  --with-pcre-jit \
  --with-http_stub_status_module \
  --with-luajit  \
  -j2  && \
  make && \
  make install && \
  make clean && \
  cd .. && \
  rm -rf ngx_openresty-*&& \
  ln -s /opt/openresty/nginx/sbin/nginx /usr/local/bin/nginx && \
  ln -sf /opt/openresty/nginx /opt/nginx && \
  ldconfig

#RUN wget https://github.com/pintsized/lua-resty-http/archive/master.zip && \
#unzip master.zip && \
#cp lua-resty-http-master/lib/resty/*.lua /opt/openresty/lualib/resty/ && \
#rm -rf master.zip lua-resty-http-master && \
RUN mkdir /opt/openresty/nginx/conf/extra-locations.d

WORKDIR /opt/openresty

#ADD nginx-conf /opt/nginx/conf

ADD https://gist.githubusercontent.com/pahud/336d63b4e14ed2a9f288/raw/2398011714298fc83228b67362f649e44b0d16fa/nginx.conf%20for%20supervisor /etc/supervisor/conf.d/nginx.conf

ADD nginx.conf.d/nginx.conf /opt/openresty/nginx/conf/nginx.conf
ADD nginx.conf.d/default.conf /opt/openresty/nginx/conf/sites-enabled.d/default.conf
ADD startup.sh /startup.sh

RUN sed -ie 's/worker_processes.*/worker_processes auto;/g'  /opt/nginx/conf/nginx.conf && \
chmod +x /startup.sh


EXPOSE 80 443

CMD ["/startup.sh"]
#CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf",  "--nodaemon"]
