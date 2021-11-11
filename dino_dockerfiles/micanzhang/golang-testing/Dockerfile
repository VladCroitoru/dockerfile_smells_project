FROM golang:1.15

LABEL maintainer="Mican Zhang <micanzhang@gmail.com>"

RUN apt-get update && apt-get install gcc libc-dev
ADD install.sh install.sh
ADD coverage.sh /usr/bin/coverage
RUN /bin/sh install.sh && rm install.sh

WORKDIR $GOPATH
