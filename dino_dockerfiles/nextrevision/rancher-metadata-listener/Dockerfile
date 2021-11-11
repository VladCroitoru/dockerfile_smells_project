FROM golang:1.6

EXPOSE 80

RUN go get github.com/rancher/rancher-metadata
RUN cd /go/src/github.com/rancher/rancher-metadata && \
    git checkout 0.7.0 && \
    go install

COPY answers.yaml /go/
ENTRYPOINT ["/go/bin/rancher-metadata"]
