# Ubuntu Base image description
#   docker build -t elarasu/weave-ubuntu .
#
FROM ubuntu:14.04
MAINTAINER elarasu@outlook.com

# Set locale
RUN locale-gen --no-purge en_US.UTF-8

# env variables
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive

# Core updates
RUN  apt-get update \
  && apt-get install -yq wget curl netcat openssl unzip sysstat lsof strace tcpdump dnsutils vim-tiny git --no-install-recommends \
  && sed -i '/ENABLED/ s/false/true/' /etc/default/sysstat \
  && apt-get autoremove -y \
  && apt-get clean -y \
  && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*
