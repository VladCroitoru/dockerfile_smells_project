FROM golang:1.8.1

WORKDIR /go/src/github.com/minodisk/presigner

RUN go get -u \
      github.com/golang/dep/...
COPY . .
RUN go install .

CMD presigner
