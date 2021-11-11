FROM golang:1.9-alpine

ENV DEP_VERSION 0.4.1

RUN apk add --no-cache git curl \
    && curl -sSL -o /usr/local/bin/dep https://github.com/golang/dep/releases/download/v${DEP_VERSION}/dep-linux-amd64 \
    && chmod +x /usr/local/bin/dep

ENTRYPOINT ["dep"]