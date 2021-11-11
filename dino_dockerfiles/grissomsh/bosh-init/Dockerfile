FROM ubuntu:14.04
MAINTAINER grissomsh wang.tianqing.cn@gmail.com

ENV REFRESH_TIME 2015-7-7

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update
RUN apt-get install -y wget
RUN wget http://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz
RUN tar -xzf go1.4.2.linux-amd64.tar.gz
RUN mv go /usr/local/go
RUN wget https://s3.amazonaws.com/bosh-init-artifacts/bosh-init-0.0.70-linux-amd64
RUN chmod +x bosh-init-0.0.70-linux-amd64
RUN mv bosh-init-0.0.70-linux-amd64 /usr/local/bin/bosh-init
RUN apt-get install -y build-essential zlibc zlib1g-dev openssl libxslt-dev libxml2-dev libssl-dev libreadline6 libreadline6-dev libyaml-dev libsqlite3-dev sqlite3 

RUN apt-get install -y ruby1.9.3 rubygems-integration

ENV GOROOT /usr/local/go
ENV GOBIN $GOROOT/bin
ENV GOPKG $GOROOT//pkg/tool/linux_amd64
ENV GOARCH amd64
ENV GOOS linux 
ENV PATH $PATH:$GOBIN:$GOPKG


RUN rm -rf  go1.4.2.linux-amd64.tar.gz

CMD ["go","help"]
