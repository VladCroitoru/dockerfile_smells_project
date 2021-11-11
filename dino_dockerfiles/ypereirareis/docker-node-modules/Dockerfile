FROM debian:8.3

MAINTAINER Yannick PEREIRA-REIS <yannick.pereira.reis@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \
  ca-certificates \
  git \
  curl \
  ssh \
  npm \
  rsync \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN npm install -g n && n stable
RUN npm install -g \
  bower \
  grunt \
  grunt-cli \
  gulp \
  gulp-cli \
  karma \
  karma-cli \
  webpack

VOLUME ["/app"]
WORKDIR /app
CMD []
