FROM ubuntu:xenial

MAINTAINER Mamut3D

LABEL Description="Openstack client tools"

RUN apt-get update && apt-get install -y \
  mc \
  vim \
  iputils-ping \
  apt-utils \
  python-dev \
  python-pip \
  python-setuptools \
  ca-certificates \
  gcc \
  musl-dev \
  && pip install --upgrade --no-cache-dir pip setuptools python-openstackclient python-keystoneclient \
  && rm -rf /var/cache/apk/*

VOLUME ["/data"]

CMD ["/bin/sh"]
