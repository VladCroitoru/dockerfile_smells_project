# builder
FROM golang:1.16-alpine AS builder

WORKDIR /app
COPY . .
RUN go mod tidy
RUN go build -o mainrun app/main.go

# runner
FROM alpine:latest
RUN apk --no-cache add ca-certificates
RUN apk update && apk upgrade && \
    apk --update --no-cache add tzdata && \
    mkdir /app

WORKDIR /app

STOPSIGNAL SIGINT
EXPOSE 8080
COPY --from=builder /app/mainrun /app
COPY --from=builder /app/.env /app
CMD /app/mainrun