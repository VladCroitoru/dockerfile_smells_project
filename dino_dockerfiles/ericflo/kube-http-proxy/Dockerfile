FROM golang:1.4.2

RUN go get github.com/constabulary/gb/...

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

COPY . /go/src/app
RUN gb build

ENTRYPOINT ["/go/src/app/bin/kube-http-proxy"]