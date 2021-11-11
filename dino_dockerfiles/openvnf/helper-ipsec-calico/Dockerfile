FROM alpine:3.7

RUN apk update && apk add jq curl

ADD run.sh /usr/local/sbin/run.sh

ENTRYPOINT run.sh
