FROM alpine:latest
MAINTAINER Ruben Vermeersch <ruben@rocketeer.be>

ENV GOROOT=/usr/lib/go \
    GOPATH=/gopath     \
    GOBIN=/gopath/bin  \
    PATH=$PATH:$GOROOT/bin:$GOPATH/bin

ADD main.go /gopath/src/github.com/rubenv/stash-go-import/

RUN apk add --update go && \
    go install -ldflags '-w -s' -v github.com/rubenv/stash-go-import && \
    apk del go && \
    mv $GOPATH/bin/stash-go-import /usr/bin/ && \
    rm -rf $GOPATH && \
    rm -rf /var/cache/apk/*

CMD ["stash-go-import"]
