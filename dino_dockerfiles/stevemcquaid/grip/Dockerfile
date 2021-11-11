# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM jfloff/alpine-python:2.7

MAINTAINER Steve McQuaid <steve@stevemcquaid.com>

# Versioning/Docker image cache reset
ENV VERSION=0.0.1

RUN pip install grip

# Document that the service listens on port 8080.
EXPOSE 8080

WORKDIR /src

CMD grip 0.0.0.0:8080