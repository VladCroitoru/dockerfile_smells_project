FROM linuxserver/baseimage
MAINTAINER Rob Shad <robertmshad@googlemail.com>
ENV APTLIST="lftp wget"

RUN apt-get update -q && \
  apt-get install $APTLIST -qy && \
  apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

ADD init/ /etc/my_init.d/
RUN chmod -v +x /etc/service/*/run && \
  chmod -v +x /etc/my_init.d/*.sh && \
   
  mkdir -p /script && \
  mkdir -p /config/lftp-output && \
  touch /script/lftp-sync-service.sh
  
# Volumes and Ports
VOLUME ["/target"]
