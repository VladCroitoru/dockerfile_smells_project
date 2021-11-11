# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang:1.11.1-alpine3.7 as builder
RUN apk add --no-cache --virtual .build-deps gcc musl-dev openssl git
RUN go get github.com/cheetahfox/player_monitoring
RUN go get github.com/PuerkitoBio/goquery
RUN go get github.com/go-sql-driver/mysql
RUN go get github.com/influxdata/influxdb/client/v2
WORKDIR /go/src/github.com/cheetahfox/player_monitoring
RUN go build
RUN strip player_monitoring

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/src/github.com/cheetahfox/player_monitoring/player_monitoring .
CMD ./player_monitoring
