# stage 0
FROM golang:latest as builder
WORKDIR /go/src/github.com/PierreZ/goStatic
COPY . .

RUN GOARCH=amd64 GOOS=linux go build  -ldflags "-linkmode external -extldflags -static -w"

# stage 1
FROM busybox
WORKDIR /
VOLUME /www
COPY --from=builder /go/src/github.com/PierreZ/goStatic/goStatic ./httpitzi
EXPOSE 80
CMD ["/httpitzi"]
