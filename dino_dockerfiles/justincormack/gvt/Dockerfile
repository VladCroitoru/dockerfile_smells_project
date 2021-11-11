FROM golang:alpine

RUN apk update && apk add git

RUN go get -u github.com/FiloSottile/gvt

WORKDIR /go/src

ENTRYPOINT ["gvt"]
