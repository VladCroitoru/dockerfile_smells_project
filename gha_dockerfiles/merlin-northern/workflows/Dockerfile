FROM golang:1.13.5-alpine3.10 as builder
RUN apk update && apk upgrade && \
    apk add \
    xz-dev \
    musl-dev \
    gcc
RUN mkdir -p /go/src/github.com/mendersoftware/workflows
COPY . /go/src/github.com/mendersoftware/workflows
RUN cd /go/src/github.com/mendersoftware/workflows && env CGO_ENABLED=1 go build

FROM alpine:3.10
RUN apk update && apk upgrade && \
        apk add --no-cache ca-certificates xz
RUN mkdir -p /etc/workflows
EXPOSE 8080
COPY ./config.yaml /etc/workflows
COPY --from=builder /go/src/github.com/mendersoftware/workflows/workflows /usr/bin
CMD ["/usr/bin/workflows", "--config", "/etc/workflows/config.yaml", "server"]
