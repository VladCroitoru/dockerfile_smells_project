FROM gliderlabs/alpine:3.4
MAINTAINER chrisurwin

EXPOSE 9777

RUN addgroup cleanup \
 && adduser -S -G cleanup cleanup

COPY ./healthcheck.go /go/src/github.com/chrisurwin/rancher-aws-host-cleanup/healthcheck.go
COPY ./rancher-aws-host-cleanup.go /go/src/github.com/chrisurwin/rancher-aws-host-cleanup/rancher-aws-host-cleanup.go

RUN apk --update add ca-certificates \
 && apk --update add --virtual build-deps go git \
 && cd /go/src/github.com/chrisurwin/rancher-aws-host-cleanup \
 && GOPATH=/go go get \
 && GOPATH=/go go build -o /bin/rancher-aws-host-cleanup \
 && apk del --purge build-deps \
 && rm -rf /go/bin /go/pkg /var/cache/apk/*

USER cleanup

ENTRYPOINT [ "/bin/rancher-aws-host-cleanup" ]