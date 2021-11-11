FROM golang:1.13.11-alpine3.11 as builder
WORKDIR /go/src/github.com/mono83/geos
COPY . .
RUN apk add --no-cache make git && make release

FROM alpine:3.11
COPY --from=builder /go/src/github.com/mono83/geos/release/geos /geos
RUN chmod a+x /geos
EXPOSE 5001 80
CMD ["/geos", ":5001", ":80"]
