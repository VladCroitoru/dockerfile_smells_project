# aws-cli docker image

FROM alpine:3.6

RUN apk update
RUN apk add bash

RUN apk --no-cache update && \
    apk --no-cache add python py-pip py-setuptools ca-certificates groff less && \
    pip --no-cache-dir install awscli && \
    rm -rf /var/cache/apk/*

RUN mkdir /root/.aws
RUN chmod 600 /root/.aws
RUN chown root:root /root/.aws
