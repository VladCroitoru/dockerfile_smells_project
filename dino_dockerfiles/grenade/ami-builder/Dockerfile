FROM alpine:latest
MAINTAINER "Rob Thijssen <rthijssen@gmail.com>"

RUN apk add --update \
    bash \
    git \
    gnupg \
    jq \
    nodejs \
    nodejs-npm \
    openssl\
    python \
    py-pip \
    util-linux \
    wget
RUN pip install --upgrade pip && pip install awscli
RUN npm install jsonlint -g
    
ENV PACKER_VERSION=1.1.3
ENV PACKER_SHA256SUM=b7982986992190ae50ab2feb310cb003a2ec9c5dcba19aa8b1ebb0d120e8686f
ADD https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip ./
ADD https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_SHA256SUMS ./
RUN sed -i '/.*linux_amd64.zip/!d' packer_${PACKER_VERSION}_SHA256SUMS
RUN sha256sum -cs packer_${PACKER_VERSION}_SHA256SUMS
RUN unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /bin
RUN rm -f packer_${PACKER_VERSION}_linux_amd64.zip
