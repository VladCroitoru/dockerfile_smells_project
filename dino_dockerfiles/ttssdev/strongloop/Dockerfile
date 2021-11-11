FROM node:7

MAINTAINER Ivo Marino <ivo.marino@ttss.ch>

LABEL Description="strongloop" Vendor="TTSS AG" Version="1.0"

ENV \
  DEBIAN_FRONTEND=noninteractive

RUN npm install -g strongloop && npm cache clear &&  \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install git -y && \
    apt-get install openssh-client
