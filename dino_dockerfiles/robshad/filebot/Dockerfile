FROM linuxserver/baseimage
MAINTAINER Rob Shad <robertmshad@googlemail.com>
ENV APTLIST="oracle-java8-installer wget"

ENV DEBIAN_FRONTEND noninteractive
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

RUN add-apt-repository ppa:webupd8team/java -y && \
  apt-get update && \
  apt-get install -y --force-yes $APTLIST && \
  apt-get clean

ADD init/ /etc/my_init.d/
RUN chmod -v +x /etc/service/*/run && \
  chmod -v +x /etc/my_init.d/*.sh && \
  mkdir -p /script && \
  mkdir -p /config && \
  touch /script/filebot-service.sh

# Volumes and Ports
VOLUME ["/input", "/output"]