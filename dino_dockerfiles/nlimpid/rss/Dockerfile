FROM golang

WORKDIR /go/src/github.com/nlimpid/rss

ADD . /go/src/github.com/nlimpid/rss

RUN go get -u github.com/golang/dep/cmd/dep

RUN /go/bin/dep ensure

RUN go build -o rss

ENTRYPOINT ["./rss"]

EXPOSE 6334
