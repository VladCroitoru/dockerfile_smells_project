FROM golang:1.9
WORKDIR /go/src/github.com/mishamx/webdump/

COPY main.go .
COPY request.go .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o webdump .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/

ENV WEBDUMP_LISTEN :3001

COPY --from=0 /go/src/github.com/mishamx/webdump/webdump .

CMD ["./webdump"]