# DOCKER_IMAGE_VERSION 21.10-252-gc84e470
FROM ubuntu:18.04

ARG BRANCH=master
RUN echo "deb http://apt.flussonic.com/repo/ ${BRANCH}/" > /etc/apt/sources.list.d/flussonic.list
COPY gpg.key /etc/apt/trusted.gpg.d/flussonic.gpg
COPY provisioner.txt /opt/flussonic/lib/online/priv/provisioner.txt

RUN apt update && apt -y install \
  flussonic-erlang=24.0.6.2 \
  flussonic-transcoder=21.08.1 \
  flussonic=21.10-252-gc84e470 && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME ["/var/log/flussonic"]
VOLUME ["/var/run/flussonic"]
VOLUME ["/etc/flussonic"]

EXPOSE 80 443 1935 554

WORKDIR /opt/flussonic
CMD ["/opt/flussonic/bin/run", \
  "--debug", \
  "-l", "/var/log/flussonic", \
  "-noinput"]
