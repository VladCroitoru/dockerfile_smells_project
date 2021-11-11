FROM golang:1.10 AS builder

WORKDIR /go/src/go-static-redirector
COPY . .

RUN go get \
    && CGO_ENABLED=0 go build

FROM busybox
COPY --from=builder /go/src/go-static-redirector/go-static-redirector /usr/bin/go-static-redirector
EXPOSE 8080
CMD ["go-static-redirector"]
