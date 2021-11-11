FROM golang:1.9.4-stretch as builder

ARG VERSION

RUN go get -u github.com/golang/dep/cmd/dep
RUN go get -u gopkg.in/alecthomas/gometalinter.v2
RUN gometalinter.v2 --install

ENV SRC_DIR /go/src/github.com/fkarakas/fizzbuzzd
WORKDIR $SRC_DIR

COPY cmd/ ./cmd
COPY pkg/ ./pkg
COPY router/ ./router
COPY Makefile ./

RUN make VERSION=${VERSION:-latest}

FROM centos:latest

COPY --from=builder /go/src/github.com/fkarakas/fizzbuzzd/fizzbuzzd /bin
RUN chmod +x /bin/fizzbuzzd

EXPOSE 8080

USER nobody
ENTRYPOINT ["fizzbuzzd"]