FROM golang:1.4.2

COPY . $GOPATH/src/github.com/stormcat24/circle-warp
WORKDIR $GOPATH/src/github.com/stormcat24/circle-warp

RUN make deps build && \
    mv ./bin/circle-warp /go/bin

ENTRYPOINT /go/bin/circle-warp

EXPOSE 8000