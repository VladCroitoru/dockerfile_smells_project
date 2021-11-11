FROM golang:1.5.3
MAINTAINER <jim@jimturpin.com>

RUN go get github.com/jturpin/rand-bug

WORKDIR /go/src/github.com/jturpin/rand-bug

EXPOSE 9090

CMD ["go", "run", "rand-bug.go"]
