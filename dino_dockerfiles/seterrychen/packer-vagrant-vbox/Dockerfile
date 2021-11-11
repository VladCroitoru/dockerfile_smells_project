FROM ubuntu:14.04.4
MAINTAINER terrychen <seterrychen@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y unzip wget openssh-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install Hashicorp tools
RUN export PACKER_VERSION=0.10.0 && \
    export VAGRANT_VERSION=1.8.1 && \
    wget --directory-prefix=/tmp https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip && \
    unzip /tmp/packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/local/bin && \
    wget --directory-prefix=/tmp https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.deb && \
    dpkg -i /tmp/vagrant_${VAGRANT_VERSION}_x86_64.deb && \
    rm -rf /tmp/*

# install Virtualbox-5.0
RUN echo "deb http://download.virtualbox.org/virtualbox/debian trusty contrib" >> /etc/apt/sources.list && \
    wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | apt-key add - && \
    wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | apt-key add - && \
    apt-get update && \
    apt-get install -y --no-install-recommends virtualbox-5.0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install build tool for Virtualbox
RUN apt-get update && \
    apt-get install -y make gcc git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
