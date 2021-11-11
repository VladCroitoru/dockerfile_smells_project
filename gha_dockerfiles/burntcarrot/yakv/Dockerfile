# Dockerfile for installing yakv

# Build the binary
FROM golang:1.16 as build
COPY . /src
WORKDIR /src
RUN CGO_ENABLED=0 GOOS=linux go build -o yakv

# Add the Alpine Linux image
FROM alpine

# Copy binary
COPY --from=build /src/yakv .

# Copy certificate and key
COPY --from=build /src/*.pem .

EXPOSE 8080
