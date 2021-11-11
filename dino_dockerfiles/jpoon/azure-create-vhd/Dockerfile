FROM golang:1.7.5-alpine3.5
MAINTAINER Jason Poon <docker@jasonpoon.ca>

ADD . /src
WORKDIR /src

RUN /src/docker-build.sh

ENTRYPOINT ["go", "run", "create_blank_vhd.go"]
