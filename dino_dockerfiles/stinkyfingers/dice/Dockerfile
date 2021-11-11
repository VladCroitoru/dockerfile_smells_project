# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

# Copy the local package files to the container's workspace.
ADD . /go/src/github.com/stinkyfingers/dice

# Build the dice command inside the container.
# (You may fetch or manage dependencies here,
# either manually or with a tool like "godep".)
RUN go get github.com/go-sql-driver/mysql
RUN go get gopkg.in/mgo.v2
RUN go get gopkg.in/mgo.v2/bson
RUN go install github.com/stinkyfingers/dice

# Run the outyet command by default when the container starts.
ENTRYPOINT /go/bin/dice

# Document that the service listens on port 8080.
EXPOSE 8080