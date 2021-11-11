FROM golang:stretch AS builder
LABEL maintainer "lennart@espe.tech" description "Admin panel for Docker Swarm"
RUN mkdir -p /go/src/github.com/lnsp/spirala
ADD . /go/src/github.com/lnsp/spirala
WORKDIR /go/src/github.com/lnsp/spirala
RUN GO111MODULE=off CGO_ENABLED=0 GOOS=linux GOARCH=amd64 \
    go build -a -installsuffix cgo -ldflags='-w -s' -o /go/bin/spirala

FROM scratch
WORKDIR /app
COPY --from=builder /go/bin/spirala /app/spirala
COPY ./layouts /app/layouts
COPY ./includes /app/includes
COPY ./static /app/static
ENTRYPOINT ["/app/spirala"]
CMD ["-H", "unix:///var/run/docker.sock"]
