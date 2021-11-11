FROM golang:alpine as builder

COPY . /go/src/github.com/rafikn/flowdock-notification-resource
COPY ./vendor/src/github.com/blang/semver /go/src/github.com/blang/semver

ENV CGO_ENABLED 0

RUN go build -o /assets/in github.com/rafikn/flowdock-notification-resource/cmd/in
RUN go build -o /assets/out github.com/rafikn/flowdock-notification-resource/cmd/out
RUN go build -o /assets/check github.com/rafikn/flowdock-notification-resource/cmd/check


WORKDIR github.com/rafikn/flowdock-notification-resource

FROM alpine:edge AS resource

RUN apk add --update --no-cache ca-certificates
RUN apk add curl

COPY --from=builder assets/ /opt/resource/
RUN chmod +x /opt/resource/*

COPY --from=builder /go/src/github.com/rafikn/flowdock-notification-resource/version /opt/resource/
ENV VERSIONPATH /opt/resource/version
