From centos:6

MAINTAINER shamaton

# define
ARG go_ver="1.10.4"

# root work
RUN yum update -y
RUN yum install -y sudo
RUN useradd -m -d /home/docker -s /bin/bash docker && echo "docker:docker" | chpasswd
RUN echo "docker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# install latest stable git
RUN yum -y install \
    git \
    gcc \
    curl-devel \
    expat-devel \
    gettext-devel \
    openssl-devel \
    zlib-devel \
    perl-ExtUtils-MakeMaker && \
    git clone https://github.com/git/git.git && \
    cd git/ && \
    git checkout `git tag | sort -V | grep -v "\-rc" | tail -1` && \
    yum -y remove git  && \
    make prefix=/usr all && \
    make prefix=/usr install && \
    cd / && \
    rm -rf /git

# install golang
RUN curl -O https://storage.googleapis.com/golang/go${go_ver}.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go${go_ver}.linux-amd64.tar.gz && \
    rm go${go_ver}.linux-amd64.tar.gz

# change user docker
WORKDIR /home/docker
USER docker

# user work
ENV PATH $PATH:/usr/local/go/bin
RUN mkdir -p ${HOME}/.packages
ENV GOPATH /home/docker/.packages
