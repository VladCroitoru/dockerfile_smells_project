FROM golang:1.9.2 as builder
WORKDIR /go/src/github.com/scalify/http-dump/

COPY . ./
RUN CGO_ENABLED=0 go build -a -ldflags '-s' -installsuffix cgo -o bin/http-dump http_dump.go

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/src/github.com/scalify/http-dump/bin/http-dump /bin/http-dump
RUN chmod +x /bin/http-dump
ENTRYPOINT ["/bin/http-dump"]
