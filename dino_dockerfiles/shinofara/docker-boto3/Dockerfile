FROM alpine:3.4
MAINTAINER Yuki Shinohara <shinofara+docker@gmail.com>

RUN apk update && \
    apk upgrade && \
    apk add --update build-base py-pip && \
    rm -rf /var/cache/apk/*

RUN pip install boto3 pyyaml

RUN adduser -S worker
USER worker

WORKDIR /work