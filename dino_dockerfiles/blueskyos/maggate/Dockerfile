FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y ca-certificates wget curl

RUN wget https://minergate.com/download/deb-cli && \
    dpkg -i deb-cli
