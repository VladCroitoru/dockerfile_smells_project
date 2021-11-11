FROM golang:1.10.0 as builder

WORKDIR /go/src/github.com/harlow/nsqd-discovery
COPY . .

RUN go get -u -v github.com/golang/dep/cmd/dep
RUN dep ensure -v
RUN CGO_ENABLED=0 go build -a --installsuffix cgo --ldflags="-s" -o nsqd-discovery

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/src/github.com/harlow/nsqd-discovery/nsqd-discovery /usr/local/bin/nsqd-discovery
ENTRYPOINT ["nsqd-discovery"]
