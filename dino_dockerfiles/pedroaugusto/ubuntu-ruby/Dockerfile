FROM ubuntu:latest

MAINTAINER Pedro Benevides <pedro.augusto.sb@gmail.com>

RUN apt-get -y update && apt-get -y install build-essential zlib1g-dev libssl-dev libreadline6-dev libyaml-dev wget

# Install ruby 2.1.4 without use rvm
RUN wget http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.4.tar.gz && \
    tar -xvzf ruby-2.1.4.tar.gz && \
    cd ruby-2.1.4/ && \
    ./configure --prefix=/usr/local --disable-install-doc && \
    make && \
    make install

# Clean the house
RUN rm ruby-2.1.4.tar.gz && rm -r ruby-2.1.4 && \
    rm -rf /var/lib/apt/lists/*
