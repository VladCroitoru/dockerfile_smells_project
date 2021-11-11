FROM golang:1.17.2 AS builder
WORKDIR /go/src/github.com/afritzler/garden-universe
RUN go get github.com/rakyll/statik
COPY . .
RUN make

FROM alpine:3.14.2
RUN apk --no-cache add ca-certificates=20191127-r5
WORKDIR /
COPY --from=builder /go/src/github.com/afritzler/garden-universe/garden-universe .
ENTRYPOINT [ "/garden-universe"]