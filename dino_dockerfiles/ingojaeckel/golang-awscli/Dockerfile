FROM golang:alpine
LABEL version="0.3"
LABEL description="This image provides a number of tools to build & deploy Go applications to AWS: go, awscli, less, bash, git, jq, file, curl"
MAINTAINER ingo.jaeckel@gmail.com
RUN apk --no-cache update && \
    apk --no-cache add python py-pip py-setuptools ca-certificates groff less bash git jq file curl && \
    pip --no-cache-dir install awscli && \
    rm -rf /var/cache/apk/*
