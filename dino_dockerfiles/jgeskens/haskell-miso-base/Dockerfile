FROM ubuntu:xenial

RUN apt-get update && apt-get install -y curl libncurses5-dev nodejs-legacy

RUN curl -sSL https://get.haskellstack.org/ | sh

ADD ./app /app

WORKDIR /app

ENV STACK_ROOT=/root/.stack
RUN mkdir -p /root/.stack && echo "\n\nallow-different-user: true\n" > /root/.stack/config.yaml

RUN stack setup
# RUN stack build

