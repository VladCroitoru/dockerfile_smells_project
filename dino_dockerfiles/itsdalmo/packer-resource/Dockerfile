FROM golang:1.10 as builder
MAINTAINER itsdalmo
ADD . /go/src/github.com/itsdalmo/packer-resource
WORKDIR /go/src/github.com/itsdalmo/packer-resource
ENV TARGET linux
ENV ARCH amd64
RUN make build

FROM hashicorp/packer:1.2.3 as resource
COPY --from=builder /go/src/github.com/itsdalmo/packer-resource/check /opt/resource/check
COPY --from=builder /go/src/github.com/itsdalmo/packer-resource/in /opt/resource/in
COPY --from=builder /go/src/github.com/itsdalmo/packer-resource/out /opt/resource/out

FROM resource
