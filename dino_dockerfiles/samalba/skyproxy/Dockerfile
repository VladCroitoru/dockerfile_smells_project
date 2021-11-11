FROM golang:1.5-alpine
COPY . /go/src/github.com/samalba/skyproxy
WORKDIR /go/src/github.com/samalba/skyproxy
ENV CODE /go/src/github.com/samalba/skyproxy
RUN set -ex \
    && buildDeps='git make' \
    && apk add --update $buildDeps \
    && rm -rf /var/cache/apk/* \
    && go get -u github.com/tools/godep \
    && make build \
    && apk del $buildDeps
ENTRYPOINT ["./skyproxy"]
