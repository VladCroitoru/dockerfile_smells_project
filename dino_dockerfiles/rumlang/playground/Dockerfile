FROM golang:1.9

RUN mkdir -p /go/src/github.com/rumlang/playground
ADD  ./ /go/src/github.com/rumlang/playground
WORKDIR /go/src/github.com/rumlang/playground
RUN go build
CMD ["./playground"]
