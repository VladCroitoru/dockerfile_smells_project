FROM golang

RUN go get golang.org/x/net/websocket
RUN go get gopkg.in/mcuadros/go-syslog.v2

ADD . /go/src/github.com/smwa/peep.js
ADD ./static /go/bin/static

RUN go install github.com/smwa/peep.js

ENTRYPOINT /go/bin/peep.js
WORKDIR /go/bin

EXPOSE 8080 2000
