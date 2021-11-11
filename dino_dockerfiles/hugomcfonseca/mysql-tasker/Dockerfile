FROM golang:alpine3.7 as builder

LABEL maintainer="Hugo Fonseca <https://github.com/hugomcfonseca/mysql-tasker>"

WORKDIR /go/src/github.com/hugomcfonseca/mysql-tasker/app/

COPY app/ .

RUN \
    apk add --update --no-cache git \
    && go get -d -v \
    && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o mysql_tasker .

FROM alpine:3.7

LABEL maintainer="Hugo Fonseca <https://github.com/hugomcfonseca/mysql-tasker>"

ENV \
    DB_HOST='localhost' \
    DB_PORT='3306' \
    DB_NAME='test' \
    DB_USER='root' \
    DB_PASS=''

COPY --from=builder /go/src/github.com/hugomcfonseca/mysql-tasker/app/mysql_tasker /usr/local/bin/

ENTRYPOINT [ "mysql_tasker" ]
