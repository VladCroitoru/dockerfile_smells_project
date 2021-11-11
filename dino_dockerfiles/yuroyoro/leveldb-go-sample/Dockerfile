FROM ubuntu:12.04
MAINTAINER yuroyoro


RUN apt-get -y update
RUN apt-get -y install sudo openssh-server
RUN apt-get -y install git
RUN apt-get -y install curl
RUN apt-get -y install golang
RUN apt-get -y install gcc
RUN apt-get install -y python-software-properties
RUN add-apt-repository ppa:openstack-ubuntu-testing/grizzly-trunk-testing
RUN apt-get -y update
RUN apt-get -y install libleveldb-dev

RUN cd /usr/local/src/ && git clone git://github.com/yuroyoro/leveldb-go-sample.git
RUN cd /usr/local/src/leveldb-go-sample && go build

RUN echo "/usr/local/src/leveldb-go-sample/leveldb-go-sample 2>&1 | tee /var/log/leveldb-go-sample.log &" > /usr/local/src/leveldb-go-sample/run.sh && chmod +x /usr/local/src/leveldb-go-sample/run.sh

