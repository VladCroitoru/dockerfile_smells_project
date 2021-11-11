FROM golang:1.15.7 as builder

WORKDIR /go/src

COPY go.mod go.sum ./
RUN go mod download

COPY . .

ARG CGO_ENABLED=0
ARG GOOS=linux
ARG GOARCH=amd64
RUN go build \
    -o /go/bin/aws-rds-maxcon-prometheus-exporter \
    -ldflags '-s -w'

FROM alpine:3.13.0 as runner

COPY --from=builder /go/bin/aws-rds-maxcon-prometheus-exporter /app/aws-rds-maxcon-prometheus-exporter

RUN adduser -D -S -H exporter

USER exporter

ENTRYPOINT ["/app/aws-rds-maxcon-prometheus-exporter"]
