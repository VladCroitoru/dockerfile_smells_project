FROM golang:1.11-alpine as builder

RUN apk add --no-cache --update ca-certificates git
ADD . /go/src/github.com/yaproxy/yap/

ENV CGO_ENABLED=0 GO111MODULE=on
RUN cd /go/src/github.com/yaproxy/yap/ && \
    go mod download && \
    go build -o yap cli/main.go

FROM alpine:3.8

RUN apk add --no-cache --update ca-certificates && \
    mkdir /yap

COPY --from=builder /go/src/github.com/yaproxy/yap/yap /usr/local/bin/
WORKDIR /yap

CMD ["/usr/local/bin/yap"]
