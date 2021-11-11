# syntax=docker/dockerfile:1.2

# Image page: <https://hub.docker.com/_/golang>
FROM --platform=${TARGETPLATFORM:-linux/amd64} golang:1.17.2-alpine as builder

RUN set -x \
    && mkdir /src \
    # SSL ca certificates (ca-certificates is required to call HTTPS endpoints)
    && apk add --no-cache ca-certificates \
    && update-ca-certificates

WORKDIR /src

COPY . .

# arguments to pass on each go tool link invocation
ENV LDFLAGS="-s -w"

RUN set -x \
    && go version \
    && CGO_ENABLED=0 go build -trimpath -ldflags "$LDFLAGS" -o /tmp/arduino-deps-installer ./cmd/arduino-deps-installer/ \
    && /tmp/arduino-deps-installer -h

# prepare rootfs for runtime
RUN mkdir -p /tmp/rootfs

WORKDIR /tmp/rootfs

RUN set -x \
    && mkdir -p \
        ./bin \
        ./tmp \
        ./etc/ssl \
        ./home/appuser \
    && cp -R /etc/ssl/certs ./etc/ssl/certs \
    && echo 'appuser:x:10001:10001::/home/appuser:/sbin/nologin' > ./etc/passwd \
    && echo 'appuser:x:10001:' > ./etc/group \
    && chown 10001:10001 ./home/appuser \
    && chmod 777 ./tmp \
    && mv /tmp/arduino-deps-installer ./bin/arduino-deps-installer

# use empty filesystem
FROM scratch

LABEL \
    org.opencontainers.image.title="arduino-deps-installer" \
    org.opencontainers.image.description="Arduino sketch dependencies installer" \
    org.opencontainers.image.url="https://github.com/tarampampam/arduino-deps-installer" \
    org.opencontainers.image.source="https://github.com/tarampampam/arduino-deps-installer" \
    org.opencontainers.image.vendor="Tarampampam" \
    org.opencontainers.image.licenses="MIT"

# Import from builder
COPY --from=builder /tmp/rootfs /

# Use an unprivileged user
USER appuser:appuser

ENTRYPOINT ["/bin/arduino-deps-installer"]

