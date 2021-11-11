FROM golang:1.6.3-alpine

RUN apk update \
    && apk add --no-cache openssh ca-certificates \
    && rm -rf /var/cache/apk/*

ADD . /go/src/github.com/karlkfi/slack-overflow-news
RUN go install ./...

ENTRYPOINT ["/go/bin/slack-overflow-news"]