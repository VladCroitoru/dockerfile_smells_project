FROM ubuntu:xenial-20170510
MAINTAINER Lun-Yuan Lee <lunyuanlee@gmail.com>
# set environment variable
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV TERM linux
ENV LC_ALL C

RUN sed -i 's/archive\.ubuntu\.com/tw\.archive\.ubuntu\.com/' /etc/apt/sources.list
RUN sed -i 's/security.ubuntu.com/free.nchc.org.tw/g' /etc/apt/sources.list

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends vim.tiny wget sudo net-tools ca-certificates apt-transport-https \
 && rm -rf /var/lib/apt/lists/*

ENV LC_ALL en_US.UTF-8

