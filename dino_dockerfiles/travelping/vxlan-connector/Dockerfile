FROM alpine:3.7

RUN apk update && apk add iproute2

ADD run.sh /usr/local/sbin/run.sh

CMD run.sh
