FROM golang:latest as builder
ENV CGO_ENABLED=0
RUN go get -v "github.com/tsaikd/gobuilder"
ADD . /go/src/github.com/tsaikd/godson
WORKDIR /go/src/github.com/tsaikd/godson
RUN gobuilder --check --test --all

FROM alpine:latest
MAINTAINER tsaikd <tsaikd@gmail.com>
RUN apk --no-cache add bash curl git rsync openssh
COPY --from=builder /go/src/github.com/tsaikd/godson/godson /usr/local/bin/godson
ENTRYPOINT ["godson"]
