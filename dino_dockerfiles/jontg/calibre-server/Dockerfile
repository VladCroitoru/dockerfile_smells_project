FROM ubuntu:14.04
MAINTAINER jon.gretarsson@gmail.com

RUN apt-get update -y && \
    apt-get install -y calibre && \
    apt-get purge -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8080

RUN mkdir /opt/calibre && mkdir /opt/calibre/library

VOLUME      ["/opt/calibre/library"]
ENTRYPOINT  ["/usr/bin/calibre-server", "--with-library=/opt/calibre/library"]
