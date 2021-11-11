## -*- docker-image-name: "btcd:0.12.0-beta" -*-
FROM golang:1.9-stretch

MAINTAINER lucianocallero@gmail.com

RUN go env GOROOT GOPATH

RUN go get -u github.com/Masterminds/glide \
&& git clone https://github.com/btcsuite/btcd $GOPATH/src/github.com/btcsuite/btcd \
&& cd $GOPATH/src/github.com/btcsuite/btcd \
&& glide install \
&& go install . ./cmd/... \
&& btcd --version \
&& cd $GOPATH/src/github.com/btcsuite/btcd \
&& git pull && glide install \
&& go install . ./cmd/... \
&& btcctl --version

ENTRYPOINT ["btcd"]
