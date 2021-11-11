FROM debian:jessie
MAINTAINER Marek Fajkus <marek.faj@gmail.com>

# Install node.js 4.x
RUN \
    apt-get update -y \
&&  apt-get install -y curl \
&&  curl -sL https://deb.nodesource.com/setup_4.x | bash - \
&&  apt-get install -y nodejs

# Clean
RUN \
    apt-get remove -y curl \
&&  apt-get clean

# install supervisor
RUN \
  npm install supervisor -g

# Test
RUN node -v
