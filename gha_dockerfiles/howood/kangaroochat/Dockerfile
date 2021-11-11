FROM golang:1.14 AS build-env

WORKDIR /go/src/github.com/howood/kangaroochat

ADD application /go/src/github.com/howood/kangaroochat/application
ADD domain /go/src/github.com/howood/kangaroochat/domain
ADD kangaroochat /go/src/github.com/howood/kangaroochat/kangaroochat
ADD infrastructure /go/src/github.com/howood/kangaroochat/infrastructure
ADD interfaces /go/src/github.com/howood/kangaroochat/interfaces
ADD library /go/src/github.com/howood/kangaroochat/library
ADD templates /go/templates
ADD go.mod /go/src/github.com/howood/kangaroochat/go.mod
ADD go.sum /go/src/github.com/howood/kangaroochat/go.sum


RUN \
     cd /go/src/github.com/howood/kangaroochat/kangaroochat &&  \
     export GO111MODULE=on && CGO_ENABLED=0 go install


FROM busybox
COPY --from=build-env /etc/ssl/certs /etc/ssl/certs
COPY --from=build-env /go/bin/kangaroochat /usr/local/bin/kangaroochat
COPY --from=build-env /go/templates /go/templates
ENTRYPOINT ["/usr/local/bin/kangaroochat"]