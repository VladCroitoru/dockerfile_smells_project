FROM ubuntu:16.04

MAINTAINER Darren Jones version: 0.3

RUN apt-get update && apt-get install -y git wget && apt-get clean && rm -rf /var/lib/apt/lists/*i && \
    wget https://github.com/geofffranks/spruce/releases/download/v1.16.2/spruce-linux-amd64 && \
        cp spruce-linux-amd64 /usr/local/bin/spruce
RUN chmod a+x /usr/local/bin/spruce && \
    rm -rf spruce-linux-amd64

