# Freestore
#
# Version 1

# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

MAINTAINER Mateus Braga <mateus.a.braga@gmail.com>

# Copy the local package files to the container's workspace.
#ADD . /go/src/github.com/mateusbraga/freestore

# Build freestore inside the container.
RUN go get -u github.com/mateusbraga/freestore/...
RUN go install github.com/mateusbraga/freestore/...

# By default, launch freestore server on port 5000
CMD ["/go/bin/freestored", "-bind", ":5000"]

#expose freestore port
EXPOSE 5000

