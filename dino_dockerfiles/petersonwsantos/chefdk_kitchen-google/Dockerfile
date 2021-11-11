FROM ubuntu:16.04

LABEL maintainer="peterson W Santos <opeterson@hotmail.com>"
LABEL chefdf.version="2.3.4"
LABEL gcloud.version="178.0.0"
LABEL tag="1.0"

ENV DEBIAN_FRONTEND noninteractive
ENV CHEFDK_VERSION 2.3.4
ENV CLOUD_SDK_VERSION 178.0.0
ARG INSTALL_COMPONENTS

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
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && apt-get install -y google-cloud-sdk=${CLOUD_SDK_VERSION}-0 $INSTALL_COMPONENTS && \
    curl https://omnitruck.chef.io/install.sh | bash -s -- -P chefdk -c stable -v $CHEFDK_VERSION && \
    echo 'eval "$(chef shell-init bash)"' >> ~/.bash_profile && \
    echo 'export PATH="/opt/chefdk/embedded/bin:$PATH"' >> ~/.bashrc && \
    chef gem install kitchen-google -v 1.4.0 && \
    apt-get install -f && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /cookbook
