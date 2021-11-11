FROM golang:1.10 as builder
MAINTAINER itsdalmo
ADD . /go/src/github.com/itsdalmo/ami-resource
WORKDIR /go/src/github.com/itsdalmo/ami-resource
ENV TARGET linux
ENV ARCH amd64
RUN make build

FROM alpine:latest as resource
RUN apk add --no-cache --update ca-certificates
COPY --from=builder /go/src/github.com/itsdalmo/ami-resource/check /opt/resource/check
COPY --from=builder /go/src/github.com/itsdalmo/ami-resource/in /opt/resource/in
COPY --from=builder /go/src/github.com/itsdalmo/ami-resource/out /opt/resource/out

FROM resource
