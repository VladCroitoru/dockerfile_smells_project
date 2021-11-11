FROM golang:1.16 AS builder

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN CGO_ENABLED=0 GOOS=linux go build -o rest_server ./cmd/rest

## -----------------------------------------

FROM alpine:latest AS production

COPY --from=builder /app .

CMD ["./rest_server"]