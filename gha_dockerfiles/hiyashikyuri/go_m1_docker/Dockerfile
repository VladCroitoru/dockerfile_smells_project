# Dockerfile
FROM golang:1.16

COPY . /app
WORKDIR /app

RUN go get -u github.com/cosmtrek/air
RUN go mod download

