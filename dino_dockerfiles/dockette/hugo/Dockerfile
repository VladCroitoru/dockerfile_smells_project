FROM dockette/alpine:3.11

RUN apk update && \
    apk upgrade && \
    apk --no-cache add hugo && \
    rm -rf /var/cache/apk/*

WORKDIR /srv

ENTRYPOINT ["/usr/bin/hugo"]
