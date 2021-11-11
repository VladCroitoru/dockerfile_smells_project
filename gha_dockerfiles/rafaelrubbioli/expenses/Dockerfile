FROM golang:alpine as builder

COPY . /app

WORKDIR /app
ENV GO112MODULE=on

RUN CGO_ENABLED=0 go build -o expenses cmd/server/server.go

FROM alpine

RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*
COPY  --from=builder /app/expenses .

CMD ["./expenses"]