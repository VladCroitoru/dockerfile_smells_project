FROM golang:1.17.0

ADD ./ $GOPATH/src/github.com/kakakikikeke/memo
WORKDIR $GOPATH/src/github.com/kakakikikeke/memo

RUN go mod tidy
RUN go build

CMD ["./memo"]