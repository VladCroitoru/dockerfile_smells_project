FROM golang

RUN go get github.com/hirokidaichi/resizing-worker

ENTRYPOINT /go/bin/resizing-worker httpserver

# Document that the service listens on port 8080.
EXPOSE 8080
