FROM golang:latest AS builder

ADD . /go/src/github.com/dutchcoders/slackarchive-import
WORKDIR /go/src/github.com/dutchcoders/slackarchive-import

ARG LDFLAGS=""
RUN go build -tags="" -o /go/bin/app github.com/dutchcoders/slackarchive-import/cmd/

FROM debian
RUN apt-get update && apt-get install -y ca-certificates
COPY --from=builder /go/bin/app /slackarchive/import

RUN mkdir /config

ENTRYPOINT ["/slackarchive/import", "--config", "/config/config.yaml"]

