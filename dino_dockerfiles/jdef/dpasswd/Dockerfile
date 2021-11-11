FROM golang:1.10.1
WORKDIR /go/src/github.com/jdef/dpasswd
COPY . .
RUN env CGO_ENABLED=0 go build -o /dpasswd .

FROM alpine:latest
WORKDIR /root/
COPY --from=0 /dpasswd .
ENTRYPOINT ["./dpasswd"]
CMD []
