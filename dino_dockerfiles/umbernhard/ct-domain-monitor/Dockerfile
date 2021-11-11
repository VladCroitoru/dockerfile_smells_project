FROM golang 

MAINTAINER Matt Bernhard

ADD . /go/src/github.com/ct-domain-monitor 

RUN go install github.com/ct-domain-monitor 

ENTRYPOINT /go/bin/ct-domain-monitor
