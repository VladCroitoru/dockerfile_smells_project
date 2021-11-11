FROM alpine:3.4
RUN apk add --no-cache curl
RUN curl -Lo /usr/bin/spruce https://github.com/geofffranks/spruce/releases/download/v1.16.2/spruce-linux-amd64 \
  && chmod +x /usr/bin/spruce
WORKDIR /root