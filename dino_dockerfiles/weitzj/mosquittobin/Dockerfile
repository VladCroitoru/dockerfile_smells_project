FROM centos:centos7
MAINTAINER Jan Weitz <me@janweitz.de>
RUN yum --quiet install -y tar \
      git \
      gcc \
      gcc-c++ \
      make \
      cmake \
      openssl-static \
      libcurl-devel \
      libuuid-devel \
      c-ares-devel && \
      cd /tmp && curl -s -O http://git.warmcat.com/cgi-bin/cgit/libwebsockets/snapshot/libwebsockets-1.3-chrome37-firefox30.tar.gz && \
      tar xzf libwebsockets-1.3-chrome37-firefox30.tar.gz && \
      cd libwebsockets-1.3-chrome37-firefox30 && mkdir build && cd build && cmake .. && make && make install && cp lib/libwebsockets.so* /lib64/ && \
      cd /tmp && git clone http://git.eclipse.org/gitroot/mosquitto/org.eclipse.mosquitto.git mosquitto && cd mosquitto && \
      git pull && git checkout 1.4 && \
      sed -i 's/WITH_WEBSOCKETS:=no/WITH_WEBSOCKETS:=yes/' config.mk && \
      make binary && cp src/mosquitto /usr/local/bin/ && cp mosquitto.conf /usr/local/etc/ && \
      cd /tmp && git clone https://github.com/weitzj/mosquitto-auth-plug.git && cd mosquitto-auth-plug && \
      cp config.mk.in config.mk && \
      sed -i 's/BACKEND_MYSQL ?= yes/BACKEND_MYSQL ?= no/' config.mk && \
      sed -i 's/BACKEND_HTTP ?= no/BACKEND_HTTP ?= yes/' config.mk && \
      sed -i 's/MOSQUITTO_SRC =/MOSQUITTO_SRC = \/tmp\/mosquitto/' config.mk && \
      make && cp auth-plug.so /lib64/ && \
      useradd mosquitto && \
      yum --quiet remove -y tar \
      git \
      gcc \
      gcc-c++ \
      make \
      cmake \
      openssl-static \
      libcurl-devel \
      libuuid-devel \
      c-ares-devel && \
      rm -rf /tmp/*

