FROM alpine:3.3

RUN set -ex \
    && export GOPATH=/go \
    && export PATH=$GOPATH/bin:/usr/local/go/bin:$PATH \
    \
    && apk add --no-cache git go \
    && go get github.com/constabulary/gb/... \
    \
    && go get github.com/kelseyhightower/confd \
    && cd $GOPATH/src/github.com/kelseyhightower/confd/ \
    && go build \
    && cp confd /usr/local/bin/editd \
    \
    && git clone https://github.com/thavel/editd.git /tmp/editd/ \
    && cd /tmp/editd/ \
    && gb vendor restore \
    && gb build \
    && cp /tmp/editd/bin/editd /usr/local/bin/editd \
    \
    && apk del openssl ca-certificates libssh2 curl expat pcre git go \
    && rm -rf /usr/local/go/ /go/ \
    && rm -rf /var/cache/apk/*
