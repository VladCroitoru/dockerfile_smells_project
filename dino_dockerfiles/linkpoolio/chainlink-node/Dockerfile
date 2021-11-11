FROM golang:1.10-alpine

RUN apk add --no-cache make gcc musl-dev git openssl bzr \ 
    && go get -u github.com/golang/dep/cmd/dep

RUN go get github.com/smartcontractkit/chainlink

WORKDIR /go/src/github.com/smartcontractkit/chainlink
RUN git pull
RUN make install
RUN go build -o /bin/chainlink

RUN rm -rf /go/src

CMD ["chainlink", "node"]
