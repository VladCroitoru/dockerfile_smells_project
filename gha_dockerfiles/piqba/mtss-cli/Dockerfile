# syntax=docker/dockerfile:1

FROM golang:1.16-alpine


WORKDIR /app

# Download necessary Go modules
COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY . ./

RUN go build -ldflags "-s -w"  -o /mtssapi cmd/api/main.go

ENV PORT=4000
ENV DB_SERVER_URL="host=0.0.0.0 port=5432 user=qwerty password=password dbname=mtss sslmode=disable"
ENV DB_MAX_CONNECTIONS=100
ENV DB_MAX_IDLE_CONNECTIONS=10
ENV DB_MAX_LIFETIME_CONNECTIONS=2

EXPOSE 4000

CMD [ "/mtssapi" ]
