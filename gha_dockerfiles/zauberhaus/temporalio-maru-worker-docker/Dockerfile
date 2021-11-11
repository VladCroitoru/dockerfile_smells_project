FROM alpine as builder

RUN apk update && apk add binutils ca-certificates && rm -rf /var/cache/apk/*

COPY ./build /build
COPY detect.sh /

RUN /detect.sh

FROM alpine:3.13 AS bench-worker

RUN apk update && apk upgrade --no-cache && rm -rf /var/cache/apk/*

COPY --from=builder /temporal-bench /usr/local/bin/

ENV NAMESPACE default
ENV FRONTEND_ADDRESS 127.0.0.1:7233
ENV NUM_DECISION_POLLERS 100
ENV TLS_CA_CERT_FILE ""
ENV TLS_CLIENT_CERT_FILE ""
ENV TLS_CLIENT_CERT_PRIVATE_KEY_FILE ""

# Base64 equivalents of above
ENV TLS_CA_CERT_DATA ""
ENV TLS_CLIENT_CERT_DATA ""
ENV TLS_CLIENT_CERT_PRIVATE_KEY_DATA ""
ENV TLS_ENABLE_HOST_VERIFICATION "false"

ENTRYPOINT ["/usr/local/bin/temporal-bench"]
