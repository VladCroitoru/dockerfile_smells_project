FROM alpine:3.5
MAINTAINER Leif Gensert <leif@leif.io>

ADD wait-for-it.sh /usr/local/bin/wait-for-it

RUN apk add --no-cache bash

ENTRYPOINT ["/usr/local/bin/wait-for-it"]
