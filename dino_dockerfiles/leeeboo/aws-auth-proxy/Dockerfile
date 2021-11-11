FROM golang:1.9.2-alpine3.7
MAINTAINER leeeboo

RUN apk --update add git glide ca-certificates

RUN mkdir -p $GOPATH/src/github.com/leeeboo

WORKDIR $GOPATH/src/github.com/leeeboo
ADD . ./aws-auth-proxy
WORKDIR ./aws-auth-proxy
RUN glide install
RUN go install github.com/leeeboo/aws-auth-proxy

ENTRYPOINT ["aws-auth-proxy"]
