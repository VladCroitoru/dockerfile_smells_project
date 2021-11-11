FROM golang:1.13 AS builder
WORKDIR /go/src/app
COPY . .
RUN go get -d -v ./...
RUN go install -v ./...

FROM debian:stable-slim
COPY --from=builder /go/bin/app .
ENTRYPOINT ["/app"]
