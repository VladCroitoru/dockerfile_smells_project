# Dockerfile References: https://docs.docker.com/engine/reference/builder/
# This file uses a go image to build the binary, this allows any envirnment to build
# the binaries, this step culd be skipped
ARG golang_binary

# Start from the latest golang base image
FROM golang:1.14 as builder
ENV GO111MODULE=on
# Set the Current Working Directory inside the container
WORKDIR /app
# Copy go mod and sum files
COPY go.mod go.sum ./
# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download
COPY . .
## Copy the source from the current directory to the Working Directory inside the container
# Build the Go app
# amd64 = x86-64
# ldfalgs -w -s remvoe debug and pproff tools
# installsuffics remove local directory names from exceptions
# CGO_ENABLED=0 disables cross compiling
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-w -s" -installsuffix cgo -o  main ./cmd
######## Start a new stage from scratch #######
FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
# Copy the Pre-built binary file from the previous stage
COPY --from=builder /app/main .
COPY ./pkg/database/migrations ./app/database/migrations
EXPOSE 8082
# Command to run the executable
CMD ["./main"]
