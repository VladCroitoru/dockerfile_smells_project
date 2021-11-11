FROM golang:1.17-alpine AS builder

# Create a workspace for the app
WORKDIR /bld

RUN apk update && apk add --no-cache git ca-certificates
RUN CGO_ENABLED=0 GOOS=linux go install github.com/grpc-ecosystem/grpc-health-probe@latest

# Download necessary Go modules
COPY go.mod .
COPY go.sum .
RUN go mod download

# Copy over the source files
COPY ./ ./

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -v -o /main

FROM gcr.io/distroless/base-debian10 AS runner

WORKDIR /

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /main /main
COPY --from=builder /go/bin/grpc-health-probe /bin/grpc-health-probe

USER 1000:1000

ENTRYPOINT ["/main"]