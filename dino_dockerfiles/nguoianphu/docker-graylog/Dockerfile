# Dockerfile for Graylog
# Graylog v2.0.3
# Date 2016-08-22

# Build with:
# docker build -t "graylog" .

# FROM debian:jessie
# FROM buildpack-deps:jessie-curl
FROM java:8-jre
# OS is Debian

MAINTAINER Tuan Vo <vohungtuan@gmail.com>

####################################################
########               Java              ###########
####################################################
# OpenJDK - Java 8

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre

####################################################
#########              GoSU             ###########
####################################################
ENV GOSU_VERSION 1.9
### install gosu 1.9 for easy step-down from root
### https://github.com/tianon/gosu/releases

RUN set -x \
  && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture)" \
  && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture).asc" \
  && export GNUPGHOME="$(mktemp -d)" \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
  && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
  && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
  && chmod +x /usr/local/bin/gosu \
  && gosu nobody true
  
####################################################
#########              Graylog            ##########
####################################################

ENV GRAYLOG_VERSION 2.0.3
# https://www.graylog.org/download

RUN set -x \
  && apt-get update \
  && apt-get dist-upgrade -y \
  && rm -rf /var/lib/apt/lists/*

RUN set -x \
  && addgroup --gid 1100 graylog \
  && adduser --disabled-password --disabled-login --gecos '' --uid 1100 --gid 1100 graylog \
  && mkdir /usr/share/graylog \
  && wget -O /usr/share/graylog.tgz "https://packages.graylog2.org/releases/graylog/graylog-${GRAYLOG_VERSION}.tgz" \
  && tar xfz /usr/share/graylog.tgz --strip-components=1 -C /usr/share/graylog \
  && chown -R graylog:graylog /usr/share/graylog \
  && rm /usr/share/graylog.tgz

ENV PATH /usr/share/graylog/bin:$PATH
WORKDIR /usr/share/graylog

RUN set -ex \
  && for path in \
    ./data/journal \
    ./data/log \
    ./data/config \
  ; do \
    mkdir -p "$path"; \
  done

COPY config ./data/config

ENV GRAYLOG_CONF /usr/share/graylog/data/config/server.conf
ENV LOG4J "-Dlog4j.configurationFile=/usr/share/graylog/data/config/log4j2.xml"

VOLUME /usr/share/graylog/data

EXPOSE 9000 12900

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["graylogctl start"]
