FROM golang:1.8.3

WORKDIR /go/src/github.com/svenwltr/docker-mmap-test

COPY . .

RUN go-wrapper install .

CMD docker-mmap-test
