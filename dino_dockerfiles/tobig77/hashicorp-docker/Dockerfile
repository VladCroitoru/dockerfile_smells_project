FROM centos:centos7

MAINTAINER Tobias Gerschner <tobias.gerschner@gmail.com>

ENV HASHICORP_URL_PREFIX https://releases.hashicorp.com
ENV TERRAFORM_VERSION 0.6.16
ENV PACKER_VERSION 0.10.1

RUN yum -y install --setopt=tsflags=nodocs epel-release wget unzip uuid && \
    yum -y install --setopt=tsflags=nodocs python-pip && \
    yum -y update && yum clean all

RUN cd /tmp && \
    wget ${HASHICORP_URL_PREFIX}/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip && \
    unzip -x packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/local/bin/ && \
    rm -vf packer_${PACKER_VERSION}_linux_amd64.zip

RUN cd /tmp && \
    wget ${HASHICORP_URL_PREFIX}/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip -x terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin/ && \
    rm -vf terraform_${TERRAFORM_VERSION}_linux_amd64.zip

RUN pip install --compile awscli

CMD [ "/bin/bash" ]
