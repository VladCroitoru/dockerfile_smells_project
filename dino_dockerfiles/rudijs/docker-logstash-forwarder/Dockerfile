FROM ubuntu:14.04
MAINTAINER Rudi Starcevic "ooly.me@gmail.com"

ENV APT_REFRESHED_AT 2015-09-01.1
RUN apt-get -yqq update

RUN \
    useradd --comment 'LogStash Forwarder Service User' --create-home --groups adm --shell /bin/bash logstash-forwarder && \
    usermod --lock logstash-forwarder

WORKDIR /home/logstash-forwarder

RUN \
    apt-get install -y git golang && \
    git clone https://github.com/elastic/logstash-forwarder.git && \
    cd logstash-forwarder && \
    go build -o logstash-forwarder && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER logstash-forwarder

ENTRYPOINT ["./logstash-forwarder/logstash-forwarder"]
