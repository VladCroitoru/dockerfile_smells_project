FROM golang:1.7

ADD . /go/src/github.com/lwander/k8s-demo

RUN go install github.com/lwander/k8s-demo

ADD ./content /content
EXPOSE 8080

ENTRYPOINT /go/bin/k8s-demo
