## hbase standalone
FROM ubuntu:14.04
MAINTAINER nuno@tradingeconomics.com

# install requirements
ENV DEBIAN_FRONTEND noninteractive
RUN \
  apt-get update && \
  apt-get install -y g++ curl git htop man unzip make wget libssl-dev pkg-config npm nano

RUN apt-get -y install build-essential python-setuptools && \
  rm -rf /var/lib/apt/lists/* && \
  easy_install supervisor

# Install Node.js
RUN \
  cd /tmp && \
  wget http://nodejs.org/dist/v0.10.29/node-v0.10.29-linux-x64.tar.gz && \
  tar xvzf node-v0.10.29-linux-x64.tar.gz && \
  rm -f node-v0.10.29-linux-x64.tar.gz

# Add Node & npm to PATH
ENV PATH /tmp/node-v0.10.29-linux-x64/bin:$PATH

CMD ["/bin/bash"]