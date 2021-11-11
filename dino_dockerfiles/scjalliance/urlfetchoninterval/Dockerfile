# --------
# Stage 1: Build
# -------
FROM golang:alpine as builder

RUN apk --no-cache add git

WORKDIR /go/src/github.com/scjalliance/urlfetchoninterval
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

COPY --from=builder /go/bin/urlfetchoninterval /

ENTRYPOINT ["/urlfetchoninterval"]
