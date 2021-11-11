# syntax=docker/dockerfile:1.2

# Image page: <https://hub.docker.com/_/golang>
FROM --platform=${TARGETPLATFORM:-linux/amd64} golang:1.17.2-alpine as builder

# can be passed with any prefix (like `v1.2.3@GITHASH`)
# e.g.: `docker build --build-arg "APP_VERSION=v1.2.3@GITHASH" .`
ARG APP_VERSION="undefined@docker"

RUN set -x \
    && mkdir /src \
    # SSL ca certificates (ca-certificates is required to call HTTPS endpoints)
    && apk add --no-cache ca-certificates \
    && update-ca-certificates

WORKDIR /src

COPY . /src

# arguments to pass on each go tool link invocation
ENV LDFLAGS="-s -w -X github.com/tarampampam/http-proxy-daemon/internal/pkg/version.version=$APP_VERSION"

RUN set -x \
    && go version \
    && CGO_ENABLED=0 go build -trimpath -ldflags "$LDFLAGS" -o /tmp/http-proxy-daemon ./cmd/http-proxy-daemon/ \
    && /tmp/http-proxy-daemon version \
    && /tmp/http-proxy-daemon -h

# prepare rootfs for runtime
RUN mkdir -p /tmp/rootfs

WORKDIR /tmp/rootfs

RUN set -x \
    && mkdir -p \
        ./etc/ssl \
        ./bin \
    && cp -R /etc/ssl/certs ./etc/ssl/certs \
    && echo 'appuser:x:10001:10001::/nonexistent:/sbin/nologin' > ./etc/passwd \
    && echo 'appuser:x:10001:' > ./etc/group \
    && mv /tmp/http-proxy-daemon ./bin/http-proxy-daemon

# use empty filesystem
FROM scratch

ARG APP_VERSION="undefined@docker"

LABEL \
    # Docs: <https://github.com/opencontainers/image-spec/blob/master/annotations.md>
    org.opencontainers.image.title="http-proxy-daemon" \
    org.opencontainers.image.description="Docker image with HTTP proxy daemon" \
    org.opencontainers.image.url="https://github.com/tarampampam/http-proxy-daemon" \
    org.opencontainers.image.source="https://github.com/tarampampam/http-proxy-daemon" \
    org.opencontainers.image.vendor="tarampampam" \
    org.opencontainers.version="$APP_VERSION" \
    org.opencontainers.image.licenses="MIT"

# Import from builder
COPY --from=builder /tmp/rootfs /

# Use an unprivileged user
USER appuser:appuser

# Docs: <https://docs.docker.com/engine/reference/builder/#healthcheck>
HEALTHCHECK --interval=15s --timeout=3s --start-period=1s CMD [ \
    "/bin/http-proxy-daemon", "healthcheck", \
    "--log-json", \
    "--port", "8080" \
]

ENTRYPOINT ["/bin/http-proxy-daemon"]

CMD ["serve", "--log-json"]
