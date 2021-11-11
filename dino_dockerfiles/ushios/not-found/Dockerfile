FROM golang:alpine
MAINTAINER UshioShugo<ushio.s@gmail.com>

EXPOSE 8080

ADD . /go/src/github.com/ushios/not-found
RUN go install github.com/ushios/not-found

ENTRYPOINT ["/go/bin/not-found", "-port", "8080", "-healthcheck", "hc"]
