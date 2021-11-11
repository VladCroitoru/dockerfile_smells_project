FROM ubuntu:trusty-20161214
#MAINTAINER Fabricio Nogueira nogsantos@gmail.com

RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \
 && echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y vim.tiny wget sudo net-tools lsof bash-completion ca-certificates unzip \
 && rm -rf /var/lib/apt/lists/*
