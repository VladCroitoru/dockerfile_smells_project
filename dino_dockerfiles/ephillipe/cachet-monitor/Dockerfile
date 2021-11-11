FROM golang

ADD . /go/src/github.com/ephillipe/cachet-monitor
RUN go install github.com/ephillipe/cachet-monitor

ENTRYPOINT /go/bin/cachet-monitor
