
FROM golang
MAINTAINER Øyvind Skaar (@oyvindsk)

# Dockerfile to build and run the API Server & Worker
# Just one docker image for both, for simplicity

# There's an official docker image for nsq. see README.md

# Expects to find the code as it is in the git repo, e.g., a api-server.go and a verify-worker.go file and the verify package

# This version builds the go code when we create the image, as opposed to when we create the container

COPY    .   /go/src/github.com/oyvindsk/go-email-address-check/
WORKDIR /go/src/github.com/oyvindsk/go-email-address-check/
RUN     go get -d -v
RUN     go build api-server.go      common.go
RUN     go build verify-worker.go   common.go

# This is hacky, since go install does not work, because I'm too lazy to make common.go a real package
RUN     mv api-server verify-worker /go/bin

