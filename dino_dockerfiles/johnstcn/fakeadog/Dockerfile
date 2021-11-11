FROM golang:alpine as builder
WORKDIR /go/src/github.com/johnstcn/fakeadog
ADD . /go/src/github.com/johnstcn/fakeadog
RUN set -x && \
    apk add -q --update && \
    apk add -q tree
RUN set -x && \
    go version && \
    go env && \
    tree /go && \
    CGO_ENABLED=0 go test -v ./... && \
    CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo github.com/johnstcn/fakeadog/cmd/fakeadog

FROM alpine:latest
MAINTAINER Cian Johnston <public@cianjohnston.ie>

ENV HOST 0.0.0.0
ENV PORT 8125
EXPOSE 8125/udp

WORKDIR /root
COPY --from=builder /go/src/github.com/johnstcn/fakeadog/fakeadog .

CMD ["./fakeadog"]
