FROM ubuntu:latest

ENV GOSS_VER v0.3.4
ENV PATH=/goss:$PATH

RUN mkdir /goss && \
    apt-get update && \
    apt-get -y install curl && \
    curl -fsSL https://goss.rocks/install | GOSS_DST=/goss sh

VOLUME /goss

