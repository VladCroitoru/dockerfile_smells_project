# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

# Copy the local package files to the container's workspace.
# Note: COPY vs ADD: COPY is same as 'ADD', but without the tar and remote URL handling.
ADD . /go/src/github.com/vahdet/go-refresh-token-store-redis

# Build the outyet command inside the container.
# RUN set -x && go get github.com/golang/dep/cmd/dep && dep ensure -v
RUN go install github.com/vahdet/go-refresh-token-store-redis

# Run the outyet command by default when the container starts.
ENTRYPOINT /go/bin/go-refresh-token-store-redis

# Document that the service listens on port 5300.
EXPOSE 5300
