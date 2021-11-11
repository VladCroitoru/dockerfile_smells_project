FROM alpine

ARG APP_VERSION=0.1.1
ARG DOWNLOAD_URL=https://github.com/andrexus/imposm-api/releases/download/v$APP_VERSION/linux_amd64_imposm-api

LABEL maintainer="Andrew Tarasenko andrexus@gmail.com"

WORKDIR /app

RUN apk update && \
    apk add ca-certificates wget && \
    update-ca-certificates && \
    wget -q $DOWNLOAD_URL -O /app/imposm-api && \
    chmod +x /app/imposm-api && \
    rm -rf /var/cache/apk/*

ADD config.default.json /app/config.json

EXPOSE 8000

ENTRYPOINT ["/app/imposm-api"]