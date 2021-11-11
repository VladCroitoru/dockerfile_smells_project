FROM node:latest
MAINTAINER avikez@gmail.com (Dmitry Shmelev)

RUN apt-get update && apt-get install -y \
  libzmq3-dev \
  python-minimal
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
