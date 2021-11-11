# Dockerfile for ckeeper.
# Workdir is set to $GOPATH=/go.
# config file can be mapped into the /ckeeper volume

FROM golang:1.7
MAINTAINER Baohua Yang <yeasy.github.io>
ENV TZ Asia/Shanghai

RUN go get github.com/yeasy/ckeeper

RUN ln -s /$GOPATH/src/github.com/yeasy/ckeeper /ckeeper

VOLUME /ckeeper

WORKDIR /$GOPATH/src/github.com/yeasy/ckeeper

# use this in development
ENTRYPOINT ["ckeeper"]
