FROM alpine:3.4
MAINTAINER Kyle Ondy <kyle@ondy.me>

RUN apk --update add \
    bash \
    curl

ADD assign-ip /usr/local/bin/assign-ip

ENTRYPOINT [ "assign-ip" ]
