FROM golang:1.5

MAINTAINER Dave Choi

COPY . $GOPATH/src/github.com/fpgeek/docker-gc
WORKDIR $GOPATH/src/github.com/fpgeek/docker-gc

RUN go get github.com/tools/godep
RUN godep go build -o $GOPATH/bin/docker-gc

CMD $GOPATH/bin/docker-gc
