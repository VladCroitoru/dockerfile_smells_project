FROM golang

WORKDIR /gopath

ENV GOPATH=/gopath
ENV GOOS=linux
ENV GOARCH=386
ENV GO15VENDOREXPERIMENT=1

RUN go get github.com/keybase/client/go/keybase && go build -tags production github.com/keybase/client/go/keybase
