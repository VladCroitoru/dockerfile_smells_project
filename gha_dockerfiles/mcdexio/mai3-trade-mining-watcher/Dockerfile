FROM golang:1.17.1-alpine3.14 as builder
RUN apk add build-base
WORKDIR /app
COPY . .
RUN go build -o mai3-trade-mining2-api ./cmd/api

FROM alpine:3.14
WORKDIR /app
COPY --from=builder /app/mai3-trade-mining2-api .
ENTRYPOINT ["./mai3-trade-mining2-api"]
