FROM alpine:3.4

MAINTAINER enm10k <enm10k@gmail.com>

RUN apk add --no-cache --update curl git openssh py-pip rsync &&\
    apk add --no-cache fabric --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted &&\
    pip install boto3

WORKDIR /app
VOLUME "/app"
