FROM alpine:3.3

ENV LANG C

RUN apk add --no-cache bash curl jq

ADD assets/ /opt/resource/
RUN chmod +x /opt/resource/*
