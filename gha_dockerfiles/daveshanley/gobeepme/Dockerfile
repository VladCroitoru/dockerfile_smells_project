# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

RUN mkdir -p /go/src/github.com/daveshanley/gobeepme
WORKDIR /go/src/github.com/daveshanley/gobeepme

# this will ideally be built by the ONBUILD below ;)
CMD ["go-wrapper", "run"]


# Copy the local package files to the container's workspace.
ADD . /go/src/github.com/daveshanley/gobeepme


COPY . /go/src/github.com/daveshanley/gobeepme
RUN go-wrapper download
RUN go-wrapper install


# Build the outyet command inside the container.
# (You may fetch or manage dependencies here,
# either manually or with a tool like "godep".)


# Run the outyet command by default when the container starts.
ENTRYPOINT /go/bin/gobeepme -service -key=privatekey.pem -cert=fullchain.pem

# Document that the service listens on port 9443
EXPOSE 9443
