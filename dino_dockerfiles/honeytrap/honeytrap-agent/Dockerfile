FROM golang:latest AS builder

ADD . /go/src/github.com/honeytrap/honeytrap-agent
WORKDIR /go/src/github.com/honeytrap/honeytrap-agent

ARG LDFLAGS=""
RUN go build -tags="" -ldflags="$(go run scripts/gen-ldflags.go)" -o /go/bin/app github.com/honeytrap/honeytrap-agent

FROM debian
RUN apt-get update && apt-get install -y ca-certificates
COPY --from=builder /go/bin/app /honeytrap/honeytrap-agent

RUN mkdir /config /data

ENTRYPOINT ["/honeytrap/honeytrap-agent", "--config", "/config/config.toml", "--data", "/data"]

EXPOSE 8022 5900
