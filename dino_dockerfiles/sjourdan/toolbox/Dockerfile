FROM alpine:3.6
MAINTAINER Stephane Jourdan <fasten@fastmail.fm>
LABEL version="20170712"
LABEL name="toolbox"
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk --update --no-cache add \
  strace \
  bind-tools \
  netcat-openbsd \
  net-tools \
  nmap \
  curl \
  tcpdump \
  htop \
  mtr \
  iotop \
  iftop \
  iputils \
  speedtest-cli py-setuptools \
  hdparm \
  dstat@testing
COPY tests.sh /tmp/
