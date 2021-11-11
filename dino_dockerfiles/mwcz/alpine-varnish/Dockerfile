FROM alpine
MAINTAINER Michael Clayton <mclayton@redhat.com>

ENV LANG en_US.utf8

RUN apk update
RUN apk add varnish curl

ADD alpine-varnish/ /

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/start"]
