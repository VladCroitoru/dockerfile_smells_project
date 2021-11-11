FROM docker:18.02

MAINTAINER Jake Harris

RUN apk update && apk upgrade && \
    apk add --no-cache bash git curl openssh python python-dev py-pip build-base
RUN curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose
RUN pip install docker-compose
