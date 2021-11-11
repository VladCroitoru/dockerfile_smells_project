FROM ubuntu:16.04
MAINTAINER Edward Ruchevits <ruchevits@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# solc and geth (geth is used just to run attach)
RUN apt-get update      -y --ignore-missing                           && \
    apt-get install     -y software-properties-common apt-utils wget  && \
    add-apt-repository  -y ppa:ethereum/ethereum                      && \
    add-apt-repository  -y ppa:ethereum/ethereum-dev                  && \
    apt-get             -y update                                     && \
    apt-get install     -y solc geth

# TODO: run apt clean

# parity 1.4.5
RUN wget http://d1h4xl4cr1h0mo.cloudfront.net/v1.4.5/x86_64-unknown-linux-gnu/parity_1.4.5_amd64.deb && dpkg -i parity_1.4.5_amd64.deb

# tools
RUN apt-get install -y python curl git unzip
RUN apt-get install -y build-essential tcl

# node 5 from package
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -
RUN apt-get install -y nodejs
# RUN apt-get install -y redis-server

RUN npm install -g pm2 node-gyp

CMD bash