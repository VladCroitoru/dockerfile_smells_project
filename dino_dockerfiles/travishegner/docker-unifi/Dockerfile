FROM ubuntu:16.04
MAINTAINER Travis Hegner <travis.hegner@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

ADD init.sh /init.sh
ADD prep.sh /prep.sh

RUN /prep.sh

VOLUME ["/var/lib/unifi"]

EXPOSE 8080/tcp 8081/tcp 8443/tcp 8843/tcp 8880/tcp 3478/udp

WORKDIR /var/lib/unifi

ENTRYPOINT ["/bin/bash", "/init.sh"]
