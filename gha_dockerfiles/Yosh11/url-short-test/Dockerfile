FROM golang:latest

COPY . /go/src/app

WORKDIR /go/src/app

RUN go build -o apiserver ./cmd/url-short/main.go

EXPOSE 8080
