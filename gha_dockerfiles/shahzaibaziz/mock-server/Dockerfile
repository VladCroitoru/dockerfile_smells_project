
FROM golang:1.16-alpine

RUN apk add build-base

RUN mkdir /app

WORKDIR /app

ADD . /app

RUN GO111MODULE=on

COPY go.mod .

COPY go.sum .

RUN go build cmd/mock-server/main.go

CMD ["./main"]