FROM gliderlabs/alpine:3.4

ENV GOPATH /go
ENV PATH $PATH:$GOPATH/bin:$GOROOT/bin

RUN apk-install -t build-deps go git \
    && go get -u github.com/jstemmer/go-junit-report \
    && apk del --purge git
