FROM golang:1.14-alpine
MAINTAINER Roel Harbers <roelharbers@gmail.com>
# This Dockerfile builds and runs the tfit executable.
# Usage:
#   docker build -t tfit .
#   echo 'SGVsbG8sIFdvcmxkIQo=' | docker run -i --rm tfit

ENV PROJECT_PATH /workspace
ENV BUILD_PATH "$PROJECT_PATH/build"

RUN mkdir -p "$PROJECT_PATH"
WORKDIR "$PROJECT_PATH"

COPY go.mod "$PROJECT_PATH/go.mod"
RUN go mod download

COPY cmd "$PROJECT_PATH/cmd"
COPY internal "$PROJECT_PATH/internal"
RUN CGO_ENABLED=0 GOOS=linux go build -o "$BUILD_PATH/tfit" cmd/tfit/main.go

CMD "$BUILD_PATH/tfit"
