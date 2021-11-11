# Build stage
FROM golang:1.10-alpine3.7
MAINTAINER Hung-Wei Chiu <hwchiu@linkernetworks.com>

WORKDIR /go/src/github.com/hwchiu/terminator
COPY main.go /go/src/github.com/hwchiu/terminator
COPY vendor /go/src/github.com/hwchiu/terminator/vendor
COPY utils /go/src/github.com/hwchiu/terminator/utils

ENV POD_NAMESPACE default

RUN apk add --no-cache git bzr
RUN go get github.com/kardianos/govendor
RUN govendor sync
RUN go install .

ENTRYPOINT /go/bin/terminator "-namespace" "$POD_NAMESPACE" "-podName" "$POD_NAME" "-container" "$TARGET_NAME"
