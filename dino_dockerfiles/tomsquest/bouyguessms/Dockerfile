FROM golang:1.10.0-stretch as builder

# Install UPX, used below to compress the resulting binary
RUN apt-get update \
  && apt-get install -y xz-utils \
  && rm -rf /var/lib/apt/lists/*
ADD https://github.com/upx/upx/releases/download/v3.94/upx-3.94-amd64_linux.tar.xz /tmp
RUN xz -d -c /tmp/upx-3.94-amd64_linux.tar.xz | \
    tar -xOf - upx-3.94-amd64_linux/upx > /bin/upx && \
    chmod a+x /bin/upx

# Install dependencies
RUN go get -u github.com/golang/dep/cmd/dep
WORKDIR /go/src/github.com/tomsquest/bouyguessms
COPY Gopkg.* ./
RUN dep ensure -vendor-only

# Build
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo cmd/bouyguessms/main.go

# Compress the binary
RUN strip --strip-unneeded main
RUN upx main

# Final image
FROM alpine:3.7 as production

RUN apk add --no-cache ca-certificates

WORKDIR /root
COPY --from=builder /go/src/github.com/tomsquest/bouyguessms/main .
ENTRYPOINT ["./main"]
