FROM golang

ADD . /go/src/go_web_server
WORKDIR /go/src/go_web_server

RUN go get github.com/gin-gonic/gin
RUN go get github.com/gin-gonic/contrib/static
RUN go install go_web_server

ENTRYPOINT /go/bin/go_web_server

EXPOSE 8000
