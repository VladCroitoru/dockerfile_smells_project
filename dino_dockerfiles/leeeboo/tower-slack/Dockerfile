FROM golang:1.10.2 as builder

WORKDIR /go/src
COPY ./* ./

RUN make build-binary

FROM alpine:3.7

RUN apk add --update ca-certificates && rm -rf /var/cache/apk/*

COPY --from=builder /go/src/tower-slack .

ENV PORT 8080

ENTRYPOINT ["/tower-slack"]
