FROM golang:1.7
MAINTAINER Ivan Shvedunov <ishvedunov@mirantis.com>

RUN apt-get update && \
    apt-get install -y rsync && \
    mkdir -p /go/src/k8s.io && \
    go get -u github.com/jteeuwen/go-bindata/go-bindata && \
    git clone --depth 1 -b v1.6.4 https://github.com/kubernetes/kubernetes.git /go/src/k8s.io/kubernetes

WORKDIR /go/src/k8s.io/kubernetes

RUN make all WHAT=cmd/kubectl && \
    make all WHAT=vendor/github.com/onsi/ginkgo/ginkgo && \
    make all WHAT=test/e2e/e2e.test

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh
