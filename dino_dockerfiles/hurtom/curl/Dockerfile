FROM alpine:latest

LABEL maintainer "https://github.com/hurtom/"
 
RUN apk add --no-cache curl tini

ENTRYPOINT ["/sbin/tini", "--"]
