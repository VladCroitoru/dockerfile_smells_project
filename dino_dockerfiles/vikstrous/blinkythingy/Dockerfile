FROM golang:1.7.3-alpine

RUN apk add -U gcc linux-headers git libc-dev ca-certificates

ADD . /go/src/github.com/vikstrous/blinkythingy

RUN go install github.com/vikstrous/blinkythingy/cmd/blinkythingy

ENTRYPOINT ["/go/bin/blinkythingy"]
