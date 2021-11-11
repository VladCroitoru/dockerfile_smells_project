FROM golang:1.17.0-alpine3.13

RUN apk update && apk add bash
RUN apk add postgresql
RUN set -ex && apk --no-cache add sudo

WORKDIR /app/backup-scheduler

COPY . .
COPY go.mod .
COPY go.sum .

RUN go mod download
RUN go build -o binary

CMD ["/app/backup-scheduler/binary"] 