FROM busybox

MAINTAINER Gabe Gorelick

RUN mkdir -p /services

VOLUME ["/services"]
WORKDIR /services

ADD *.service /services/
ADD *.env /services/
