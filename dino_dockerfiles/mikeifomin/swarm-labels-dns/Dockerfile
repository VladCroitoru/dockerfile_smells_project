FROM golang:1.7

MAINTAINER mikeifomin@gmail.com
ENV DOCKER_HOST=unix:///var/run/docker.sock
RUN mkdir -p /app
WORKDIR /app

COPY . /app
RUN go get -d
RUN go build main.go
ENTRYPOINT ["./main"]
