FROM golang:1.11 as builder
ENV SRC_ROOT /go/src/github.com/TrilliumIT/updog
WORKDIR ${SRC_ROOT}
RUN go get -u github.com/alecthomas/gometalinter && \
	go get -u github.com/golang/dep/cmd/dep && \
	go get -u github.com/kevinburke/go-bindata/... && \
	go get -u github.com/clinta/genify
RUN gometalinter --install

ADD . ${SRC_ROOT}/
RUN dep ensure
RUN ./make.sh

FROM alpine:latest
WORKDIR /
COPY --from=builder /go/src/github.com/TrilliumIT/updog/updog .
EXPOSE 8080
CMD ["/updog"]
