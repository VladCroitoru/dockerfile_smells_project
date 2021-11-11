FROM golang

RUN apt-get update && apt-get install libpcap0.8-dev -y

ADD . /go/src/github.com/rgbkrk/pottytime

RUN go get github.com/rgbkrk/pottytime
RUN go install github.com/rgbkrk/pottytime

ENTRYPOINT ["/go/bin/pottytime"]
