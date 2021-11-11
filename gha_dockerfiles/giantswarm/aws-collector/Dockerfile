FROM golang:1.17.2 AS builder
ENV GO111MODULE=on
COPY go.mod /etc/go.mod
RUN cat /etc/go.mod | grep k8scloudconfig | awk '{print $1"/...@"$2}' | xargs -I{} go get {}
# This is needed to extract the versioned catalog name, e.g. v6@6.0.1
RUN ln -s /go/pkg/mod/$(cat /etc/go.mod | grep k8scloudconfig | awk '{print $1"@"$2}') /opt/k8scloudconfig

FROM alpine:3.14.2

RUN apk add --no-cache ca-certificates

RUN mkdir -p /opt/aws-collector
ADD ./aws-collector /opt/aws-collector/aws-collector

WORKDIR /opt/aws-collector

EXPOSE 8000
ENTRYPOINT ["/opt/aws-collector/aws-collector"]
