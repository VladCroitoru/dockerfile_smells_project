FROM gliderlabs/alpine:3.2
ENTRYPOINT ["/bin/risu"]

COPY . /go/src/github.com/wantedly/risu
RUN apk update \
      && apk upgrade \
      && apk add git go mercurial \
      && cd /go/src/github.com/wantedly/risu \
      && export GOPATH=/go \
      && go get github.com/tools/godep \
      && $GOPATH/bin/godep go build -ldflags "-X main.Version" -o /bin/risu \
      && rm -rf /go \
      && apk del --purge go mercurial
