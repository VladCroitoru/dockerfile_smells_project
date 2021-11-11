# Development environment container for server developers.
FROM alpine:latest

LABEL maintainer "alexey@slaykovsky.com"
LABEL description "Complete development environment for MD server."
LABEL version "2.0"

RUN apk update && apk upgrade
RUN apk add wget cmake make boost-dev bash gcc \
	tar mariadb-dev git qt5-qtbase-dev g++

ENV CFLAGS "-mtune=generic -march=x86-64 -m64 -Os -pipe"
ENV CXXFLAGS $CFLAGS
ENV WT_VERSION master
ENV DOCKERIZE_VERSION v0.3.0

WORKDIR /tmp
RUN wget https://github.com/emweb/wt/archive/master.tar.gz
RUN tar xf $WT_VERSION.tar.gz

RUN mkdir wt-build

WORKDIR wt-build
RUN cmake -DMYSQL_LIBRARY=mysqlclient \
	/tmp/wt-$WT_VERSION
RUN make -j$(getconf _NPROCESSORS_ONLN) install

WORKDIR /tmp
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
	&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
	&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /

RUN rm -rf /usr/{{lib,share}/locale,{lib,lib64}/gconv,bin/localedef,sbin/build-locale-archive}
RUN rm -rf /usr/share/{man,doc,info,gnome/help}
RUN rm -rf /usr/share/cracklib
RUN rm -rf /usr/share/i18n
RUN rm -rf /var/cache/*
RUN rm -rf /sbin/sln
RUN rm -rf /var/tmp/*
RUN rm -rf /tmp/*

RUN mkdir -p -m 0755 /var/cache/ldconfig
