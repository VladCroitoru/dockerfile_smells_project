# --------
# Stage 1: Build
# -------
FROM golang:alpine as builder

RUN apk update && apk --no-cache add ca-certificates openssh git

WORKDIR /go/src/github.com/scjalliance/weblm

RUN git clone https://github.com/scjalliance/weblm.git .

# Disable CGO to make sure we don't rely on libc
ENV CGO_ENABLED=0

# Exclude debugging symbols and set the netgo tag for Go-based DNS resolution
ENV BUILD_FLAGS="-v -a -ldflags '-d -s -w' -tags netgo"

RUN go get -d -v ./...
RUN go install -v ./...

# --------
# Stage 2: Release
# --------
FROM scjalliance/adskflex
MAINTAINER emmaly.wilson@scjalliance.com

COPY --from=builder /go/bin/weblm /

# add weblm port
EXPOSE 7259

# setup init script
COPY plusrun.sh /opt/

# setup init
ENTRYPOINT ["/opt/plusrun.sh"]
