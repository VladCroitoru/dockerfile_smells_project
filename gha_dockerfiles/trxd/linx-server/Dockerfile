FROM golang:1.15-alpine AS builder

RUN apk update && apk add --no-cache git

RUN go get -v github.com/andreimarcu/linx-server

FROM alpine

ENV GOPATH=/go
WORKDIR /go/src/github.com/andreimarcu/linx-server
COPY --from=builder /go/bin/linx-server /usr/local/bin/linx-server
COPY --from=builder /go/src/github.com/andreimarcu/linx-server/static ./static
COPY --from=builder /go/src/github.com/andreimarcu/linx-server/templates ./templates

WORKDIR /data/files
WORKDIR /data/meta
WORKDIR /data
EXPOSE 8080

COPY linx-server.conf /etc/linx-server.conf

CMD ["/usr/local/bin/linx-server", "-config", "/etc/linx-server.conf"]
