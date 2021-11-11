FROM golang

ADD . /go/src/github.com/willgorman/mesoscon-demo

RUN go install github.com/willgorman/mesoscon-demo

ENTRYPOINT /go/bin/mesoscon-demo
