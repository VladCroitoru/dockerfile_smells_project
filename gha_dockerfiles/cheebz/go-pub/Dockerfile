# Build stage
FROM golang:1-alpine as builder

# RUN apk update && apk add openssl
# RUN mkdir /etc/ssl/go-pub
# RUN openssl req -x509 -newkey rsa:4096 -keyout /etc/ssl/go-pub/key.pem -out /etc/ssl/go-pub/cert.pem -days 365 -nodes -subj '/CN=*'

RUN mkdir /app
WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . ./
RUN go build

# Production stage
FROM alpine:latest as prod

RUN mkdir /app
WORKDIR /app

COPY --from=builder /app/go-pub ./
# COPY --from=builder /etc/ssl/go-pub/* ./certs/

CMD [ "./go-pub" ]
