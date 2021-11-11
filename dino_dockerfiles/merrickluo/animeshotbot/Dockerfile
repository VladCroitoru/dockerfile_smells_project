FROM alpine:3.5

COPY . /go/src/github.com/merrickluo/animeshotbot
RUN apk update \
  && apk add ca-certificates \
	&& update-ca-certificates \
	&& apk add -t build-deps build-base go git mercurial \
	&& cd /go/src/github.com/merrickluo/animeshotbot \
	&& export GOPATH=/go \
	&& go get \
	&& go build -o /bin/animeshotbot \
	&& rm -rf /go \
	&& apk del --purge build-deps

CMD ["/bin/animeshotbot"]
