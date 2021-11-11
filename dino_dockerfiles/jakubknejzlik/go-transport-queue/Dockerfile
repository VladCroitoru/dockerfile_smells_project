FROM golang:alpine

RUN apk update && \
		apk add make git

COPY . $GOPATH/src/github.com/inloop/go-transport-queue

WORKDIR $GOPATH/src/github.com/inloop/go-transport-queue

RUN make install

ENTRYPOINT ["go-transport-queue"]
