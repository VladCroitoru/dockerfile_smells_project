FROM ubuntu:16.04

LABEL maintainer="peterson W Santos <opeterson@hotmail.com>"
LABEL chefdf.version="178.0.0"
LABEL awscli.version="1.11.187"
LABEL tag="1.0"

ENV DEBIAN_FRONTEND noninteractive
ENV CHEFDK_VERSION 2.3.4

RUN apt-get update -qqy && apt-get install -qqy \
        curl \
        gcc \
        python-dev \
        python-setuptools \
        apt-transport-https \
        lsb-release \
        openssh-client \
        git \
        vim \
        apt-utils \
        ca-certificates curl \
        software-properties-common \
        && easy_install -U pip && \
    pip install -U crcmod && \
    pip install -U awscli==1.11.187 && \
    curl https://omnitruck.chef.io/install.sh | bash -s -- -P chefdk -c stable -v $CHEFDK_VERSION && \
    echo 'eval "$(chef shell-init bash)"' >> ~/.bash_profile && \
    echo 'export PATH="/opt/chefdk/embedded/bin:$PATH"' >> ~/.bashrc && \
    chef gem install kitchen-ec2    -v 1.3.2 && \
    apt-get install -f && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /cookbook
