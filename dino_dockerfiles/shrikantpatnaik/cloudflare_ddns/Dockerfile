FROM golang:1.10.1 as builder
WORKDIR /go/src/github.com/shrikantpatnaik/cloudflare_ddns
RUN go get -d -v github.com/withmandala/go-log
RUN go get -d -v github.com/cloudflare/cloudflare-go
COPY main.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o cloudflare_ddns .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /go/src/github.com/shrikantpatnaik/cloudflare_ddns/cloudflare_ddns .
CMD ["./cloudflare_ddns"]
