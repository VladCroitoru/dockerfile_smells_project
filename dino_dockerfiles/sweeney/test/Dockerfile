FROM golang

ADD . /go/src/github.com/sweeney/test

RUN go install github.com/sweeney/test

ENTRYPOINT /go/bin/test

EXPOSE 8080