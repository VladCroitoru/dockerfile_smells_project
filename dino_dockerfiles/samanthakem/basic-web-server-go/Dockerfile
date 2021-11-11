FROM golang

ADD . /go/src/github.com/samanthakem/hello-go/hello

RUN go install github.com/samanthakem/hello-go/hello

ENTRYPOINT /go/bin/hello

EXPOSE 8080
