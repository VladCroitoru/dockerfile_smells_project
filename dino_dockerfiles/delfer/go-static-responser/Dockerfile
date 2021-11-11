FROM golang:1.10 AS builder

WORKDIR /go/src/go-static-responser
COPY . .

RUN go get \
    && CGO_ENABLED=0 go build

FROM busybox
COPY --from=builder /go/src/go-static-responser/go-static-responser /usr/bin/go-static-responser
EXPOSE 8080
CMD ["go-static-responser"]
