# Compiling

FROM golang:1.14-alpine as build

RUN apk update && apk upgrade && apk add git
RUN go get -u github.com/go-telegram-bot-api/telegram-bot-api

COPY notify.go notify.go

RUN go build notify.go

# Production

FROM alpine:3.11

COPY --from=build /go/notify /bin

EXPOSE 8080

CMD ["notify"]
