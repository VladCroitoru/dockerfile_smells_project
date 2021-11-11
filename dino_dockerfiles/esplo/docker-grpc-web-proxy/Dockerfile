# build stage
FROM golang:1.9.4-alpine as builder
LABEL maintainer="esplo@users.noreply.github.com"

RUN apk update && apk upgrade && \
    apk add --no-cache git openssh openssl gettext

RUN go get -u github.com/improbable-eng/grpc-web/go/grpcwebproxy

# create certificate
RUN mkdir -p /tmp/ \
    && openssl req -new -x509 -sha256 -newkey rsa:2048 -days 365 -nodes -out /tmp/localhost.crt -keyout /tmp/localhost.key -subj "/C=JP/ST=MyState/L=MyLocality/O=MyOrg/OU=dev/CN=localhost"


# deploy stage
FROM alpine:latest
LABEL maintainer="esplo@users.noreply.github.com"

COPY --from=builder /go/bin/grpcwebproxy .
COPY --from=builder /tmp/localhost.crt /tmp/localhost.key ./

CMD [ \
    "./grpcwebproxy", \
    "--server_tls_cert_file=./localhost.crt", \
    "--server_tls_key_file=./localhost.key", \
    "--backend_addr=server:50051" \
]
