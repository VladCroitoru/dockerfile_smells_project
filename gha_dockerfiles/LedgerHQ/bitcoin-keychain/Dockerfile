FROM golang:1.16-alpine as builder

# System setup
RUN apk update && apk add git curl build-base autoconf automake libtool && rm -rf /var/cache/apk/*

# Install mage
RUN mkdir /tmp/mage
WORKDIR /tmp/mage
RUN git clone https://github.com/magefile/mage && cd mage && go run bootstrap.go

RUN go install github.com/bufbuild/buf/cmd/buf@v1.0.0-rc3

WORKDIR /app

COPY go.mod .
COPY go.sum .
COPY pb/go.mod pb/
RUN go mod download

COPY . .

# Build the Go app
RUN mage -v build

# Start fresh from a smaller image
FROM alpine

RUN wget -O /bin/grpc_health_probe \
    https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/v0.4.5/grpc_health_probe-linux-386 \
    && chmod +x /bin/grpc_health_probe
COPY --from=builder /app/server /app/server

ENV GRPC_GO_LOG_SEVERITY_LEVEL info
ENV GRPC_GO_LOG_VERBOSITY_LEVEL 1

EXPOSE 50052

CMD ["/app/server"]
