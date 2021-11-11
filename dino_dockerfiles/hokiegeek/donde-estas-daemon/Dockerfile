FROM golang:alpine

RUN mkdir -p /go/src/github.com/hokiegeek/donde-estas-daemon
COPY . /go/src/github.com/hokiegeek/donde-estas-daemon

WORKDIR /go/src/github.com/hokiegeek/donde-estas-daemon

RUN go get -d -v
RUN go install -v ./...

ENTRYPOINT ["donded"]
