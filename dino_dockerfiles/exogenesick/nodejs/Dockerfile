FROM ubuntu:14.04

MAINTAINER Krzysztof Pająk <kpajak@gmail.com>

RUN apt-get install -y wget \
  curl \
  vim \
  && cd /tmp \
  && wget http://nodejs.org/dist/v0.12.0/node-v0.12.0-linux-x64.tar.gz \
  && tar -xzf node-v0.12.0-linux-x64.tar.gz \
  && mv node-v0.12.0-linux-x64 /node \
  && cd /usr/local/bin \
  && ln -s /node/bin/* .

RUN npm install -g \
  grunt-cli \
  bower \
  express-generator \
  mocha \
  gulp \
  jshint

RUN mkdir /data

RUN adduser --disabled-password --gecos '' node \
  && adduser node sudo \
  && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER node

WORKDIR /data

CMD ["/bin/bash"]
