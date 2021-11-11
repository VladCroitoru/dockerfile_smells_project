FROM golang

RUN apt-get update && apt-get install -y libwebkit2gtk-3.0-dev xvfb

RUN go get github.com/sourcegraph/go-webkit2/...
