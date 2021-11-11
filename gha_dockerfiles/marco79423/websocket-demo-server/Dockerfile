FROM golang:1.16 AS builder
ENV CGO_ENABLED=0 GOFLAGS=-mod=vendor
WORKDIR /app
COPY . .
RUN go build /app/cmd/websocket-demo-server

FROM alpine:3.12
RUN apk update && \
    apk upgrade && \
    apk add --no-cache ca-certificates && \
    apk add git

WORKDIR /app
COPY --from=builder /app/websocket-demo-server /app/websocket-demo-server

ENTRYPOINT ["/app/websocket-demo-server"]
