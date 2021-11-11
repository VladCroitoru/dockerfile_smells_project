FROM golang:alpine

ADD . /go/src/app
WORKDIR /go/src/app

RUN go build -o oc_app main.go
EXPOSE 8888

ENTRYPOINT ./oc_app_loh