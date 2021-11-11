FROM nginx:1.11.1-alpine

RUN apk add --no-cache s6 && \
    \
    apk add --no-cache go git gcc musl-dev && \
    mkdir /go && \
    export GOPATH=/go && \
    mkdir -p /go/src/github.com/kelseyhightower/ && \
    git clone https://github.com/kelseyhightower/confd /go/src/github.com/kelseyhightower/confd && \
    cd /go/src/github.com/kelseyhightower/confd && \
    git checkout -q --detach "20b3d37da7aaa2c176c0612202c06c5ba4f7d987" && \
    cp -R vendor/* /go/src/ &&\
    go build -a -installsuffix cgo -ldflags '-extld ld -extldflags -static' -x . && \
    mv ./confd /bin/ && \
    chmod +x /bin/confd && \
    apk del go git gcc musl-dev && \
    rm -rf /src

ADD root /

CMD ["s6-svscan", "/s6"]
