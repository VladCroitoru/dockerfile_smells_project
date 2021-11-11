ARG GO_VERSION=1.17

FROM golang:${GO_VERSION}-alpine AS builder

RUN apk update && apk add alpine-sdk git && rm -rf /var/cache/apk/* && mkdir -p /api

WORKDIR /api

COPY go.mod .
COPY go.sum .
RUN go mod download

COPY main.go .
COPY .env.production ./.env.default
RUN go build -o ./app ./main.go

FROM alpine:latest

RUN rm -rf /var/cache/apk/* && mkdir -p /api

WORKDIR /api
COPY --from=builder /api/app .
COPY --from=builder /api/.env.default .

EXPOSE 8080

ENTRYPOINT ["./app"]