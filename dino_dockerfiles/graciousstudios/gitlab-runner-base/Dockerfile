FROM alpine:latest
RUN apk add --no-cache --update curl bash wget tini git alpine-sdk build-base
ENTRYPOINT ["/sbin/tini", "--"]

