FROM golang:latest AS builder

WORKDIR /go/src/github.com/seriousben/whoamI

RUN go get -u github.com/golang/dep/cmd/dep

COPY . ./

RUN dep ensure && CGO_ENABLED=0 GOOS=linux go build -a .

FROM alpine:3.6 AS base

RUN apk add --update --no-cache ca-certificates

FROM scratch

HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD ["/whoamI", "healthcheck", "--port", "8080"]

COPY --from=base /etc/passwd /etc/passwd
COPY --from=base /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder /go/src/github.com/seriousben/whoamI/whoamI /whoamI
USER nobody

EXPOSE 8080
ENTRYPOINT ["/whoamI", "serve", "--port", "8080"]
