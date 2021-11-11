FROM golang:1.10 AS builder

COPY . /go/src/github.com/majst01/redis2es/
WORKDIR /go/src/github.com/majst01/redis2es/
RUN go get -u github.com/golang/dep/cmd/dep \
 && make \
 && mkdir -p /redis2es/lib \
 && cp redis2es /redis2es/ \
 && cp -a lib /redis2es/lib/

FROM debian:buster-slim
WORKDIR /redis2es
COPY --from=builder /redis2es/* /redis2es/
ENTRYPOINT ["/redis2es/redis2es"]
