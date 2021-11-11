FROM ubuntu:14.04

# Setup MongoDB sources
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y golang git mongodb-org-tools curl

# Set GOPATH
ENV GOPATH /go

# Grab Source
COPY . /go/src/github.com/scheedule/coursestore

WORKDIR /go/src/github.com/scheedule/coursestore

# Grab project dependencies and build
RUN go get ./... && go install

ENTRYPOINT ["/go/bin/coursestore"]
