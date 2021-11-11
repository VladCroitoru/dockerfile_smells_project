FROM alpine:3.6

MAINTAINER Yuta Okamoto <okapies@gmail.com>

ENV HOME /root
ENV DOCKER_ARC_URL "https://download.docker.com/linux/static/stable/x86_64"
ENV DOCKER_VERSION "18.06.1-ce"

RUN cd /tmp \
  && apk add --no-cache ca-certificates wget git \
  && update-ca-certificates \
  && wget $DOCKER_ARC_URL/docker-$DOCKER_VERSION.tgz \
  && tar xzvf docker-$DOCKER_VERSION.tgz \
  && mv docker/* /usr/local/bin \
  && rm -r docker docker-$DOCKER_VERSION.tgz
