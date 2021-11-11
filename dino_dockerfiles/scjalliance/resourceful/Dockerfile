# --------
# Stage 1: Build
# -------
FROM golang:alpine as builder

RUN apk --no-cache add git

WORKDIR /go/src/github.com/scjalliance/resourceful
COPY . .

WORKDIR /go/src/github.com/scjalliance/resourceful/cmd/resourceful

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

VOLUME /data
EXPOSE 5877

COPY --from=builder /go/bin/resourceful /

WORKDIR /data
CMD ["/resourceful", "guardian"]
