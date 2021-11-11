FROM golang:alpine AS builder

RUN apk --update add git openssh && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

COPY . /go/src/github.com/katsew/kodama

WORKDIR /go/src/github.com/katsew/kodama

RUN go install

FROM alpine:latest

COPY --from=builder /go/bin/kodama /usr/local/bin/kodama
RUN apk --update add ca-certificates iptables curl && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

ENTRYPOINT ["/usr/local/bin/kodama"]
CMD ["http", "server"]

