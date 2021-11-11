FROM ubuntu:16.04
MAINTAINER Takashi Inaba

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

RUN wget http://feed.flightradar24.com/linux/fr24feed_1.0.18-5_amd64.tgz && \
    tar xvzf fr24feed_1.0.18-5_amd64.tgz

WORKDIR /tmp/fr24feed_amd64

ENTRYPOINT ["./fr24feed"]
