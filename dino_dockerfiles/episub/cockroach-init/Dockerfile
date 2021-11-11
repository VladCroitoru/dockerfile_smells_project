# Build importer

FROM golang:1.10
ADD init.go /go/src/github.com/episub/cockroach-init/init.go
ADD init.sh /built/init.sh
WORKDIR /go/src/github.com/episub/cockroach-init
RUN go build
RUN cp cockroach-init /built/init
