FROM ubuntu:16.04

WORKDIR /usr/src/cucumber-cpp

RUN apt-get update && \
    apt-get -y install cmake build-essential ninja-build \
                       libboost-thread-dev libboost-system-dev \
                       libboost-regex-dev libboost-date-time-dev \
                       libboost-filesystem-dev libboost-program-options-dev \
                       libboost-test-dev google-mock git \
                       ruby ruby-dev

RUN git clone https://github.com/cucumber/cucumber-cpp.git .

RUN gem install bundler && \
    bundle install

