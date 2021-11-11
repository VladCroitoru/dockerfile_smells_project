FROM golang:1.8-alpine3.6

ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN apk update \
 && apk add bash curl git openssh glide ca-certificates && update-ca-certificates \
 && rm -rf /var/cache/apk/* /var/tmp/* /tmp/* \

