
FROM ubuntu:12.04

ENV DEBIAN_FRONTEND noninteractive

RUN \
  mkdir /data && \
  mkdir /data/db && \
  touch /data/db/dummy

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential software-properties-common python-software-properties curl git-core libxml2-dev libxslt1-dev libfreetype6-dev python-pip python-apt python-dev libxmlsec1-dev swig libmysqlclient-dev && \
  apt-get install -y curl git vim wget aptitude sudo && \
  rm -rf /var/lib/apt/lists/*

RUN \
  pip install --upgrade pip &&  \
  pip install --upgrade virtualenv 


WORKDIR /var/tmp

RUN git clone https://github.com/edx/configuration

WORKDIR /var/tmp/configuration

RUN \
  pip install -r requirements.txt &&  \
  pip install setuptools --upgrade

RUN \
   dd if=/dev/zero of=/swapfile bs=2G count=1
RUN \
   chmod 600 /swapfile &&  \
   mkswap /swapfile
#RUN \
#   swapon /swapfile
   
WORKDIR /var/tmp/configuration/playbooks

RUN \
   ansible-playbook -c local ./edx_sandbox.yml -i "localhost,"

EXPOSE 80 80 18010
