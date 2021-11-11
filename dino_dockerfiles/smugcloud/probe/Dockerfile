FROM alpine:latest

RUN apk update && apk add ca-certificates

COPY build/probe /usr/bin

ENTRYPOINT [ "probe" ]