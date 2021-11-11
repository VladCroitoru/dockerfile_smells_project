FROM golang:1.10.0-stretch
ENV SRC_DIR=/go/src/github.com/juntaki/firestarter-sqs-proxy
ADD . $SRC_DIR
WORKDIR $SRC_DIR

RUN cd $SRC_DIR && \
    go get -u -v && \
    go build -o main .

FROM golang:1.10.0-stretch
ENV SRC_DIR=/go/src/github.com/juntaki/firestarter-sqs-proxy
COPY --from=0 $SRC_DIR/main /app/main
CMD ["/app/main"]