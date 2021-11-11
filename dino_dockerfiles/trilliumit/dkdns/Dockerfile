FROM golang:1.13-alpine as builder
ENV SRC_ROOT /go/src/github.com/TrilliumIT/dkdns
WORKDIR ${SRC_ROOT}
ADD . ${SRC_ROOT}/
RUN go build -v -o alpine-dkdns


FROM alpine:latest
WORKDIR /
COPY --from=builder /go/src/github.com/TrilliumIT/dkdns/alpine-dkdns .

EXPOSE 53

ENTRYPOINT ["/alpine-dkdns"]
