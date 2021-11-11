FROM golang:1.16.4

# Copy the local package files to the container's workspace.
ADD . /go/src/github.com/Verseghy/matverseny-backend

# Build the outyet command inside the container.
# (You may fetch or manage dependencies here,
# either manually or with a tool like "godep".)
WORKDIR /go/src/github.com/Verseghy/matverseny-backend
RUN go build -ldflags "-s -w"

# Run the outyet command by default when the container starts.
ENTRYPOINT /go/src/github.com/Verseghy/matverseny-backend/matverseny-backend

EXPOSE 6969
