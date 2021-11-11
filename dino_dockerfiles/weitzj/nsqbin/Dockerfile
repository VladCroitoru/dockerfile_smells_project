FROM centos:centos7
MAINTAINER Jan Weitz <me@janweitz.de>
RUN yum --quiet install -y tar
RUN curl -s -O https://s3.amazonaws.com/bitly-downloads/nsq/nsq-0.3.0.linux-amd64.go1.3.3.tar.gz
RUN [ $(sha1sum nsq-0.3.0.linux-amd64.go1.3.3.tar.gz | grep -c 99d37abe54b2d10ae328c4209a95b15c5dcdec5d) == 1 ] && \
    tar xzf nsq-0.3.0.linux-amd64.go1.3.3.tar.gz && \
    mv nsq-0.3.0.linux-amd64.go1.3.3/bin/* /usr/local/bin/ && \
    rm -rf nsq-0.3.0.linux-amd64.go1.3.3*

