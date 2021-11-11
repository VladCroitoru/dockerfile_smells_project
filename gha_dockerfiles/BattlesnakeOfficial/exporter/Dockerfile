FROM golang:1.15.6-alpine as builder


COPY . /go/src/github.com/BattlesnakeOfficial/exporter/
WORKDIR /go/src/github.com/BattlesnakeOfficial/exporter

RUN CGO_ENABLED=0 GOOS=linux go install -installsuffix cgo ./cmd/...

FROM alpine:latest

RUN apk add --no-cache ca-certificates

WORKDIR /app

COPY --from=builder /go/bin/ /bin/
COPY ./render/assets/ ./render/assets/

CMD ["/bin/exporter"]
