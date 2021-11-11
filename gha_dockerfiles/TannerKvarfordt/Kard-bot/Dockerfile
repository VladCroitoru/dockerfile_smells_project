# syntax=docker/dockerfile:1

FROM golang:1.17-alpine

WORKDIR /app

COPY Robo_cat.png ./
COPY go.mod ./
COPY go.sum ./
COPY main.go ./
COPY kardbot/ ./kardbot

RUN go mod download
RUN go build -o ./Kard-bot
ENV CGO_ENABLED=0
RUN go test -v ./...

CMD [ "./Kard-bot" ]
