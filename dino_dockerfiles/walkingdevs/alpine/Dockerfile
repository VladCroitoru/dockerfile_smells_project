FROM alpine:3.9

COPY repositories /etc/apk

RUN apk update && \
    apk upgrade && \
    apk add ca-certificates && \
    apk add openssl && \
    rm -rf /var/cache/apk/*