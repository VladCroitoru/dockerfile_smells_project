# Alpine Linux with latest golang installed plus packages needed for CI builds using Drone

# See https://github.com/gliderlabs/docker-alpine/blob/master/README.md

FROM gliderlabs/alpine:3.4
MAINTAINER nycmonkey@gmail.com
ENV GOPATH /usr/lib/go
RUN apk update && apk upgrade && apk add ca-certificates git openssh-client bash go
RUN go version
