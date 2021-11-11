FROM golang

ADD . /go/src/github.com/rgbkrk/peekaboo

RUN go get github.com/rgbkrk/peekaboo
RUN go install github.com/rgbkrk/peekaboo

ENTRYPOINT ["/go/bin/peekaboo"]
