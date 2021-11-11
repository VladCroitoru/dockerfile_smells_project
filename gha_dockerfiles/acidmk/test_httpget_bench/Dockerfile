FROM golang:1.17 as builder

ENV CGO_ENABLED 0
ENV GOOS linux

WORKDIR /app
COPY . .

RUN go get -d -v
RUN go build -o test-bench

FROM alpine:3.14.2

RUN apk add --no-cache gettext libintl ca-certificates

WORKDIR /app
COPY --from=builder /app/test-bench .
COPY .env.example .

ENTRYPOINT envsubst < ./.env.example > ./.env \
    && GIN_MODE=release ./test-bench
