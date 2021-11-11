FROM golang:1.4.2-onbuild
MAINTAINER maran.hidskes@gmail.com

RUN mkdir /data
VOLUME ["/data"]
ENTRYPOINT ["/go/bin/app", "-dbDir=/data"]

EXPOSE 8080
