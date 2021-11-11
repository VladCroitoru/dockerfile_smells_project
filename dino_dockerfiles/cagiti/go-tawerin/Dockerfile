FROM golang:1.11

ADD . /go/src/go-tawerin

RUN cd /go/src/go-tawerin \
       && make build

EXPOSE 8080
WORKDIR /go/src/go-tawerin
ENTRYPOINT go run main.go app.go
