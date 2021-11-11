FROM golang:1.17 AS build-env

WORKDIR /go/src/github.com/howood/imagereductor

ADD application /go/src/github.com/howood/imagereductor/application
ADD domain /go/src/github.com/howood/imagereductor/domain
ADD imagereductor /go/src/github.com/howood/imagereductor/imagereductor
ADD infrastructure /go/src/github.com/howood/imagereductor/infrastructure
ADD interfaces /go/src/github.com/howood/imagereductor/interfaces
ADD library /go/src/github.com/howood/imagereductor/library
ADD go.mod /go/src/github.com/howood/imagereductor/go.mod
ADD go.sum /go/src/github.com/howood/imagereductor/go.sum


RUN \
     cd /go/src/github.com/howood/imagereductor/imagereductor &&  \
     export GO111MODULE=on && CGO_ENABLED=0 go install


FROM busybox
COPY --from=build-env /etc/ssl/certs /etc/ssl/certs
COPY --from=build-env /go/bin/imagereductor /usr/local/bin/imagereductor
ENTRYPOINT ["/usr/local/bin/imagereductor"]