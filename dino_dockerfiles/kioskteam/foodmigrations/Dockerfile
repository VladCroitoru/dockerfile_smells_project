FROM golang:1.3.1
MAINTAINER Mohammad Sadegh Khoeini(MSK) <mskco.tp@gmail.com>

RUN go get bitbucket.org/liamstask/goose/cmd/goose
ADD db/ /go/src/migrations/db/
WORKDIR /go/src/migrations/

ENV DATABASE_URL postgres://postgres@postgres_1/postgres?sslmode=disable

CMD goose up
