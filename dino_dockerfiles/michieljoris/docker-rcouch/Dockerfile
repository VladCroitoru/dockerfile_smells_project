FROM ubuntu:14.04

MAINTAINER Michiel van Oosten "https://github.com/michieljoris"

ENV DEBIAN_FRONTEND noninteractive

# make sure the package repository is up to date and update ubuntu
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y install wget &&  \
  locale-gen en_US.UTF-8 && \
  apt-get -y install supervisor && \
  mkdir -p /var/log/supervisor && \
  mkdir -p /etc/supervisor/conf.d && \
  apt-get install -y libcurl4-openssl-dev && \
  wget https://github.com/Michieljoris/docker-rcouch/raw/master/rcouch.tgz && \
  tar xf rcouch.tgz && rm rcouch*.tgz 

# COPY  rcouch-stock.tgz ./
# RUN  tar xf rcouch-stock.tgz && rm rcouch*.tgz

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV HOME /root

# supervisor base configuration
ADD supervisor.conf /etc/supervisor.conf

# default command
CMD ["supervisord", "-c", "/etc/supervisor.conf"]

# Expose listen port
EXPOSE 5984

# Expose our data, logs and configuration volumes
VOLUME ["/rcouch/rcouch/data", "/rcouch/rcouch/log", "/rcouch/rcouch/etc"]


COPY rcouch.conf /etc/supervisor/conf.d/rcouch.conf


