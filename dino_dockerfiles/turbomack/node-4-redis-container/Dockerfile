FROM ubuntu:14.04
MAINTAINER turbomack

# Install node.js 4.x
RUN \
    apt-get update -y \
&&  apt-get install -y curl \
&&  curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - \
&&  apt-get install -y nodejs

# Install redis
RUN \
    apt-get install -y redis-server \
&&  cp /etc/redis/redis.conf /etc/redis/redis.conf.default

# Install ruby
RUN \
    apt-get update \
&&  apt-get install -fyqq software-properties-common \
&&  apt-add-repository ppa:brightbox/ruby-ng \
&&  apt-get update \
&&  apt-get install -fyqq ruby2.2

# Install git
RUN \
    apt-get update \
&&  apt-get install -fyqq git-core

# test after install
RUN \
    node -v \
&&  npm -v \
&&  redis-server -v \
&&  ruby -v

# start redis
CMD \
    redis-server /etc/redis/redis.conf
