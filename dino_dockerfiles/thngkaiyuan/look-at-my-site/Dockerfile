FROM golang:alpine

ADD . /go/src/github.com/thngkaiyuan/look-at-my-site

RUN apk add --no-cache git
RUN go get golang.org/x/net/idna
RUN go install github.com/thngkaiyuan/look-at-my-site

ENTRYPOINT /go/bin/look-at-my-site

EXPOSE 8080
