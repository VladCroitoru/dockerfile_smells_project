FROM alpine:latest

MAINTAINER Jason Richard McNeil <jason@jasonrm.net>

COPY build.sh main.go /

RUN /bin/sh build.sh

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/heli"]
