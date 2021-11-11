# --------
# Stage 1: Build
# -------
FROM golang:alpine as builder

RUN apk --no-cache add git

WORKDIR /go/src/github.com/scjalliance/dpma-firmware-downloader
COPY . .

# Disable CGO to make sure we don't rely on libc
ENV CGO_ENABLED=0

# Exclude debugging symbols and set the netgo tag for Go-based DNS resolution
ENV BUILD_FLAGS="-v -a -ldflags '-d -s -w' -tags netgo"

RUN go get -d -v ./...
RUN go install -v ./...

# --------
# Stage 2: Release
# --------
FROM gcr.io/distroless/base

COPY --from=builder /go/bin/dpma-firmware-downloader /

ENV CONFIG_FILE=/config.json \
    FIRMWARE_DIR=/firmware \
    CACHE_DIR=/cache \
    FLATTEN=true \
    MANIFEST= \
    INCLUDE_MODELS= \
    INCLUDE_FILES= \
    EXCLUDE_MODELS= \
    EXCLUDE_FILES= \
    LATEST=

WORKDIR /firmware
WORKDIR /cache

VOLUME /firmware
VOLUME /cache

CMD ["/dpma-firmware-downloader"]
