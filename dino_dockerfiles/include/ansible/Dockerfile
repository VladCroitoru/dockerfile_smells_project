FROM ubuntu:latest
MAINTAINER include <francisco.cabrita@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    language-pack-en && \
    locale-gen en_US.UTF-8 && dpkg-reconfigure locales && \
    apt-get install -y \
    build-essential \
    gcc \
    make \
    software-properties-common && \
    apt-add-repository ppa:ansible/ansible -y && \
    apt-get update && apt-get install -y \
    ansible \
    python-dev \
    python-software-properties \
    python-simplejson \
    python-boto3 \
    python3-boto3 \
    awscli \
    wget \
    curl \
    git \
    s3cmd && \
    apt-get clean

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py

WORKDIR /ansible

ADD ./files ./files
ADD ./group_vars ./group_vars
ADD ./inventories ./inventories
ADD ./playbooks ./playbooks
ADD ./roles ./roles
ADD ./ansible.cfg ./
ADD ./site.yml ./
ADD ./ssh_config ./
