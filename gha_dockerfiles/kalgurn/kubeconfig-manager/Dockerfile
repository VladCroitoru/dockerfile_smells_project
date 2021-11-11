FROM golang:latest

COPY . /app
WORKDIR /app

RUN go mod download
RUN go test -v ./...