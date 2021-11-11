FROM golang:1.6.0-alpine
MAINTAINER Arnaud Porterie <icecrime@docker.com>

# Install GB dependency manager
RUN apk update && apk add git
RUN go get github.com/constabulary/gb/...

# Build the project
ADD . /src
WORKDIR /src
RUN gb build all

# Drop privileges
RUN adduser -D bulletin
USER bulletin

# Set the entrypoint
ENTRYPOINT ["/src/bin/vossibility-bulletin"]
