FROM golang:alpine AS builder

LABEL maintainer="Fabien Bellanger <valentil@gmail.com>"

# Set necessary environmet variables needed for our image
ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

# Move to working directory /build
WORKDIR /build

# Copy and download dependency using go mod
COPY go.mod .
COPY go.sum .
RUN go mod download

# Copy the code into the container
COPY . .

# Pkger
RUN go get github.com/markbates/pkger/cmd/pkger
RUN pkger

# Build the application
RUN go build -a -installsuffix cgo -o fiber-boilerplate .

# Move to /dist directory as the place for resulting binary folder
WORKDIR /dist

# Copy binary from build to main folder
RUN cp /build/fiber-boilerplate /build/projects.json /build/favicon.png .
RUN cp /build/config-docker.toml ./config.toml

# -----------------------------------------------------------------------------

FROM alpine:latest

LABEL maintainer="Fabien Bellanger <valentil@gmail.com>"

RUN apk update && apk --no-cache add ca-certificates

COPY --from=builder /dist/fiber-boilerplate /
COPY --from=builder /dist/config.toml /
COPY --from=builder /dist/projects.json /
COPY --from=builder /dist/favicon.png /

# Command to run
ENTRYPOINT ["./fiber-boilerplate"]

EXPOSE 9999
