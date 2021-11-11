FROM golang:alpine

ADD . /go/src/github.com/kununu/goaws

ADD ./app/conf/goaws.yaml /go/conf/goaws.yaml

RUN apk add --no-cache git mercurial \
    && go get -u github.com/kardianos/govendor \
    && cd /go/src/github.com/kununu/goaws \
    && /go/bin/govendor sync \
    && go install github.com/kununu/goaws/app/cmd \
    && apk del git mercurial

ENTRYPOINT ["/go/bin/cmd", "Local", "debug"]

EXPOSE 4100
