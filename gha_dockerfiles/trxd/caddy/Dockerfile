ARG VERSION=v2.0.0

FROM golang:1.17-alpine as builder

ARG VERSION

RUN apk add --no-cache \
    git \
    build-base \
    ca-certificates

WORKDIR /go/bin

RUN go get -u github.com/caddyserver/xcaddy/cmd/xcaddy

RUN xcaddy build ${VERSION} \
    --output /usr/bin/caddy \
    --with github.com/caddyserver/forwardproxy@caddy2=github.com/klzgrad/forwardproxy@naive \
    --with github.com/mholt/caddy-webdav \
    --with github.com/sjtug/caddy2-filter \
    --with github.com/caddy-dns/cloudflare

# Fetch the latest default welcome page and default Caddy config
FROM alpine AS fetch-assets

RUN apk add --no-cache git

ARG DIST_COMMIT=4d5728e7a4452d31030336c8e3ad9a006e58af18

WORKDIR /src/dist
RUN git clone https://github.com/caddyserver/dist .
RUN git checkout $DIST_COMMIT

RUN cp config/Caddyfile /Caddyfile
RUN cp welcome/index.html /index.html

FROM alpine AS alpine

COPY --from=builder /usr/bin/caddy /usr/bin/caddy
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs

COPY --from=fetch-assets /Caddyfile /etc/caddy/Caddyfile
COPY --from=fetch-assets /index.html /usr/share/caddy/index.html

ARG VCS_REF
ARG VERSION
LABEL org.opencontainers.image.revision=$VCS_REF
LABEL org.opencontainers.image.version=$VERSION
LABEL org.opencontainers.image.title=Caddy
LABEL org.opencontainers.image.description="a powerful, enterprise-ready, open source web server with automatic HTTPS written in Go"
LABEL org.opencontainers.image.url=https://caddyserver.com
LABEL org.opencontainers.image.documentation=https://github.com/caddyserver/caddy/wiki/v2:-Documentation
LABEL org.opencontainers.image.vendor="Light Code Labs"
LABEL org.opencontainers.image.licenses=Apache-2.0
LABEL org.opencontainers.image.source="https://github.com/caddyserver/caddy-docker"

EXPOSE 80
EXPOSE 443
EXPOSE 2019

CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]

FROM gcr.io/distroless/static

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs
COPY --from=builder /usr/bin/caddy /usr/bin/caddy

COPY --from=fetch-assets /Caddyfile /etc/caddy/Caddyfile
COPY --from=fetch-assets /index.html /usr/share/caddy/index.html

ARG VCS_REF
ARG VERSION
LABEL org.opencontainers.image.revision=$VCS_REF
LABEL org.opencontainers.image.version=$VERSION
LABEL org.opencontainers.image.title=Caddy
LABEL org.opencontainers.image.description="a powerful, enterprise-ready, open source web server with automatic HTTPS written in Go"
LABEL org.opencontainers.image.url=https://caddyserver.com
LABEL org.opencontainers.image.documentation=https://github.com/caddyserver/caddy/wiki/v2:-Documentation
LABEL org.opencontainers.image.vendor="Light Code Labs"
LABEL org.opencontainers.image.licenses=Apache-2.0
LABEL org.opencontainers.image.source="https://github.com/caddyserver/caddy-docker"

EXPOSE 80
EXPOSE 443
EXPOSE 2019

ENTRYPOINT ["caddy"]
CMD ["run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
