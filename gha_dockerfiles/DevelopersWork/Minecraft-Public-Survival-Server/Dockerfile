FROM openjdk:16-jdk-alpine

RUN apk add python3 py3-pip python3-dev gcc

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN apk update && \
    apk add --no-cache bash && \
    rm -rf /var/cache/apk/* /tmp/* /var/tmp/* $HOME/.cache