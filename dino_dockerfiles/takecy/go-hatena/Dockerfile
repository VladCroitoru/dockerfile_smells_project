FROM golang

MAINTAINER takecy

RUN go version
RUN go env

ENV DEBUG *

COPY . $GOPATH/src/github.com/takecy/go-hatena
WORKDIR $GOPATH/src/github.com/takecy/go-hatena

RUN go get github.com/tools/godep
RUN godep restore

CMD ["go", "test", "./hatena/*.go", "-v"]
