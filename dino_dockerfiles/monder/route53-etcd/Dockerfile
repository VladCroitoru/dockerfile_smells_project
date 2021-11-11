FROM golang:1.5

ENV GO15VENDOREXPERIMENT=1
RUN go get github.com/Masterminds/glide

RUN mkdir -p /go/src/github.com/monder/route53-etcd
WORKDIR /go/src/github.com/monder/route53-etcd
COPY . /go/src/github.com/monder/route53-etcd
RUN glide install && go build

ENTRYPOINT ["/go/src/github.com/monder/route53-etcd/route53-etcd"]
