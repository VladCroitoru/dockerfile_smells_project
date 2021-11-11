# Multi stage buils FTW!: https://blog.docker.com/2017/07/multi-stage-builds/
FROM golang:1.9 AS builder
MAINTAINER Leandro López (inkel) <leandro@citrusbyte.com>

WORKDIR /go/src/lruc

ADD ["main.go", "."]

# Compile an optimized version to be deployed as a Docker container
# # https://medium.com/@kelseyhightower/optimizing-docker-images-for-static-binaries-b5696e26eb07
ENV CGO_ENABLED=0 GOOS=linux
RUN ["go", "build", "-a", "-tags", "netgo", "-ldflags", "'-w'", "."]

# Final container image
FROM scratch
COPY --from=builder /go/src/lruc/lruc /lruc

EXPOSE 8080

ENTRYPOINT ["/lruc"]
