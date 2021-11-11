FROM golang:1.9-alpine

ENV DEP_VERSION 0.4.1

RUN \
  apk add --no-cache ca-certificates curl git mercurial openssh &&\
  go get -u github.com/Masterminds/glide &&\
  go get -u github.com/tebeka/go2xunit &&\
  go get -u github.com/onsi/ginkgo/ginkgo
ADD https://github.com/golang/dep/releases/download/v${DEP_VERSION}/dep-linux-amd64 /usr/local/bin/dep

RUN chmod +x /usr/local/bin/dep
