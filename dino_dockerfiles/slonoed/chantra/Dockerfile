FROM golang:1.8-alpine

ENV GO_ENV=production

ADD . /go/src/github.com/slonoed/chantra
WORKDIR /go/src/github.com/slonoed/chantra

RUN go build
RUN go install

EXPOSE 3000

CMD ["chantra"]
