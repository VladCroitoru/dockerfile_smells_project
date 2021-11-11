FROM alpine:latest
MAINTAINER Andreas Krüger

RUN apk add --update mysql-client

WORKDIR /
RUN mkdir /sql

COPY sql/ /sql
COPY run.sh /run.sh

ENTRYPOINT ["/run.sh"]
