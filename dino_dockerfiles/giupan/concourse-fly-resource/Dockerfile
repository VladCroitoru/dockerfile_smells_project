FROM alpine:edge
MAINTAINER Giuseppe La Tona <giuseppelatona@gmail.com>

COPY assets/* /opt/resource/

RUN apk add --no-cache \
    ca-certificates \
    curl \
    jq \
    openssh \
    openssl \
 && update-ca-certificates
