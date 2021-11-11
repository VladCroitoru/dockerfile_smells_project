FROM golang:1.4

RUN mkdir -p /go/src/github.com/syb-devs/goose

COPY . /go/src/github.com/syb-devs/goose

RUN cd /go/src/github.com/syb-devs/goose/http/server/api && go get && go build -o /go/bin/api .

RUN cd /go/src/github.com/syb-devs/goose/http/server/file && go get && go build -o /go/bin/goose .

ENV PORT 80
EXPOSE 80

WORKDIR /go/bin

CMD goose