FROM golang:1.10 as builder
WORKDIR /go/src/app
COPY . .
RUN go get -d -v ./...
RUN CGO_ENABLED=0 go build -tags=netgo -ldflags="-X main.BUILD=$(date -u +%Y-%m-%dT%H:%M:%SZ)"

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root
COPY --from=builder /go/src/app/app .
COPY --from=builder /go/src/app/bunnyhop.yml /etc/
CMD ["./app"]
