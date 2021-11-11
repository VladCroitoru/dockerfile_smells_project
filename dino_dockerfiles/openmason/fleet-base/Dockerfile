# Base image description
#
# Usage:
# docker build -t openmason/fleet-base .
#
#
FROM ubuntu:14.04
MAINTAINER el aras<openmason@gmail.com>

# Set locale
RUN locale-gen --no-purge en_US.UTF-8

# env variables 
ENV HOME /root
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive
#ENV DEPLOY_USER openmason

# Core updates
RUN \
  apt-get update; \
  apt-get install -yq  build-essential git  software-properties-common libevent-dev libzmq-dev --no-install-recommends; 

# Any ppa repositories go here

# Python, Useful tools / system utilities
RUN \
  apt-get install -yq python python-dev python-setuptools python-pip --no-install-recommends; \
  apt-get install -yq openssh-server \
      wget curl unzip sysstat lsof strace tcpdump dnsutils \
      --no-install-recommends; 

# node.js 
RUN \
  curl -sL https://deb.nodesource.com/setup | sudo bash -; \
  apt-get install -yq nodejs --no-install-recommends; 

RUN \
  easy_install -U pip; \
  pip install --upgrade circus; 
#  npm install -g chevron; 

# clustering base
#RUN \
#  cd /tmp; \
#    wget https://dl.bintray.com/mitchellh/consul/0.5.0_linux_amd64.zip -O consul.zip; \
#    unzip consul.zip; \
#    chmod +x consul; \
#    mv consul /usr/local/bin; \
#    wget -O /usr/local/bin/confd https://github.com/kelseyhightower/confd/releases/download/v0.9.0/confd-0.9.0-linux-amd64; \
#    chmod +x /usr/local/bin/confd; 

RUN \
  sed -i '/ENABLED/ s/false/true/' /etc/default/sysstat; \
  sed -i '/PermitRootLogin/ s/without-password/yes/' /etc/ssh/sshd_config; \
  mkdir -p \
    /etc/consul.d \
    /var/run/sshd \
    /var/log/circus;

# Everything is controled via mozilla circus supervisor
ADD circus/circusd.conf  /etc/circusd.conf
ADD logrotate/circus     /etc/logrotate.d/circus

# All cleanups
RUN apt-get clean; \
  rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* 

RUN echo 'root:nosamnepo' | chpasswd

# Expose ports
EXPOSE 22

# Set the default command to execute
# when creating a new container
CMD ["/usr/local/bin/circusd", "/etc/circusd.conf"]

