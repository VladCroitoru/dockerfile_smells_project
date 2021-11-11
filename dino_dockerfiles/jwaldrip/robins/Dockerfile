FROM golang:latest
MAINTAINER Jason Waldrip <jason@waldrip.net>

# Add
ADD . $GOPATH/src/github.com/jwaldrip/robins
WORKDIR $GOPATH/src/github.com/jwaldrip/robins

# Get Deps
RUN go get

# Run CMD
ENTRYPOINT ["robins"]
