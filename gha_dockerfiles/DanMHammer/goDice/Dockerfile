FROM golang:alpine as builder
RUN apk --no-cache add ca-certificates git
WORKDIR /build/app

# Fetch dependencies
COPY app/go.mod ./
RUN go mod download

# Test
COPY app/. ./
RUN CGO_ENABLED=0 GOOS=linux GARCH=amd64 go test ./app/..

# Build
RUN CGO_ENABLED=0 GOOS=linux GARCH=amd64 go build

# Create final image
FROM alpine
WORKDIR /root
COPY --from=builder /build/app/dice .
EXPOSE 3000
ENTRYPOINT ["./dice"]
