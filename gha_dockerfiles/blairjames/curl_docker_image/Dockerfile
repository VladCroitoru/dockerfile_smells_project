FROM alpine:latest
RUN apk update && apk upgrade && \
    apk add --no-cache curl libcurl curl-static curl-doc curl-dbg
ENTRYPOINT ["/usr/bin/curl"]
