# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md
# We start with the phusion base image since it gets us a builtin, pre-configured
# daemon manager (runit) and a logging framework (syslog-ng) for free
FROM phusion/baseimage:0.9.18
MAINTAINER LeisureLink Tech <techteam@leisurelink.com>
# The original, in a private LeisureLink repository was Michael Hughes <mhughes@leisurelink.com>

ENV NODE_VERSION 4.2.4

ADD https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz /tmp/node-v${NODE_VERSION}-linux-x64.tar.gz

RUN set -ex && \
  cd /tmp && \
  tar -xzf /tmp/node-v${NODE_VERSION}-linux-x64.tar.gz -C /usr/local --strip-components=1 && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* \
         /var/tmp/* \
         /tmp/*
