# source: https://blog.golang.org/docker

# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

RUN mkdir -p /go/src/app

# Copy the local package files to the container's workspace.
ADD ./src/chat_server /go/src/app


# Environment Variables
#ENV HOST_IP=""
#ENV TCP_PORT="3333"
#ENV API_PORT="5555"

# Document that the service listens on port 3333 (TCP Accept).
EXPOSE 3333

# Document that the service listens on port 5555 (HTTP API).
EXPOSE 5555

# Build the compiled chat_server command inside the container.
# (You may fetch or manage dependencies here,
# either manually or with a tool like "godep".)
RUN go build -o /go/bin/chat_server /go/src/app/*.go

# Run the outyet command by default when the container starts.
ENTRYPOINT /go/bin/chat_server
