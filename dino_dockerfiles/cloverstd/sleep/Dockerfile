FROM golang:1.9-alpine

RUN apk --no-cache add ca-certificates wget && \
    mkdir -p /go/src/github.com/cloverstd && \
    wget -q -O /go/src/github.com/cloverstd/sleep.tar.gz https://github.com/cloverstd/sleep/archive/master.tar.gz && \
    cd /go/src/github.com/cloverstd && \
    tar zxf sleep.tar.gz && mv sleep-master sleep && \
    cd sleep && go build && mv sleep /usr/local/bin/sleep-web && \
    cd / && \
    rm -rf /go/* && \
    apk del ca-certificates wget && \
    rm -rf /var/cache/*

EXPOSE 1234
CMD ["sleep-web"]
