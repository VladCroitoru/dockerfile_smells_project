FROM debian:stable
MAINTAINER Rohit Hinduja

RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir /nodejs && curl -k https://nodejs.org/dist/latest/node-${VERSION:-$(curl -sk https://nodejs.org/dist/latest/ | sed -nr 's|.*>node-(.*)\.pkg</a>.*|\1|p')}-linux-x64.tar.gz | tar xvzf - -C /nodejs --strip-components=1

ENV PATH $PATH:/nodejs/bin
