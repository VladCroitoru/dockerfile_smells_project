FROM alpine:latest
MAINTAINER Serge Ovchinnikov <sovchinn@gmail.com>

RUN apk --no-cache add \
      bash \
      py-pip \
      python &&\
    pip install --upgrade \
      pip \
      awscli &&\
    mkdir ~/.aws

# Expose volume for adding credentials VOLUME ["~/.aws"]
VOLUME ["~/.aws"]
