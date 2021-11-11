FROM google/golang:latest

MAINTAINER theMagicalKarp

WORKDIR /gopath/src/github.com/theMagicalKarp/octant

ADD . /gopath/src/github.com/theMagicalKarp/octant/

RUN go get github.com/theMagicalKarp/octant

ENTRYPOINT ["/gopath/bin/octant"]