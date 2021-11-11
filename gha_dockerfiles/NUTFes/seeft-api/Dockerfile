FROM golang:1.16.3

ENV GO111MODULE=on
ENV GOPATH=/go

WORKDIR /go/src/github.com/NUTFes/seeft

RUN go get github.com/cosmtrek/air

CMD air
