FROM ubuntu:12.04
MAINTAINER BuiltDock Project <info@builtdock.com>

ENV DEBIAN_FRONTEND noninteractive

# teh deps
RUN apt-get update && apt-get install -yq \
    make \
    ca-certificates \
    net-tools \
    sudo \
    wget \
    vim \
    strace \
    lsof \
    netcat \
    --no-install-recommends

# generate a local to suppress warnings
RUN locale-gen en_US.UTF-8

# download latest stable etcdctl
ADD https://s3-us-west-2.amazonaws.com/opdemand/etcdctl-v0.4.5 /usr/local/bin/etcdctl
RUN chmod +x /usr/local/bin/etcdctl

# install confd
ADD https://s3-us-west-2.amazonaws.com/opdemand/confd-v0.5.0-json /usr/local/bin/confd
RUN chmod +x /usr/local/bin/confd
