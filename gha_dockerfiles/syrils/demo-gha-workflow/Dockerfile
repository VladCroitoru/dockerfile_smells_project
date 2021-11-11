FROM golang:alpine AS base

#Set necessary env vars for the image
ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

WORKDIR /build

# Copy and download dependency using go mod
COPY go.mod .
COPY go.sum .
RUN go mod download

# Copy the code into the container
COPY . .

# Build the application
RUN go build -o main .

# Move to /app directory as the place for resulting binary folder
WORKDIR /app

# Copy binary from build to main folder
RUN cp /build/main .

# Build a small image
FROM alpine:latest

RUN apk --no-cache add ca-certificates

# Copy the Pre-built binary file from the previous stage
COPY --from=base /app/main .

# Command to run
ENTRYPOINT ["./main"]