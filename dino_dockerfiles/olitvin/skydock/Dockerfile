FROM golang:1.10.1-alpine

RUN apk upgrade --update musl \
    && apk add \
       git \
       rsyslog \
    && rm -rf /var/cache/apk/*

# go get to download all the deps
RUN go get -u -v github.com/olitvin/skydock

ADD . /go/src/github.com/olitvin/skydock
ADD ./slog /go/src/github.com/olitvin/skydock/slog
ADD ./docker /go/src/github.com/olitvin/skydock/docker
ADD plugins/ /plugins

RUN export GOROOT=/go

RUN cd /go/src/github.com/olitvin/skydock && go install -v . ./...

ENTRYPOINT ["/go/bin/skydock"]
