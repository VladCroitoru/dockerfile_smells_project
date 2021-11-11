FROM docker
LABEL maintainer: docker@irespaldiza.com

RUN apk --update add py-pip &&\
     rm -rf /var/cache/apk/*
RUN pip install docker-compose
