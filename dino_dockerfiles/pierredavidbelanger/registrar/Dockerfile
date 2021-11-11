FROM alpine:3.7
ENTRYPOINT ["/usr/local/bin/registrar"]

COPY . /go/src/github.com/pierredavidbelanger/registrar
RUN apk --no-cache add -t build-deps build-base go git \
	&& apk --no-cache add ca-certificates \
	&& cd /go/src/github.com/pierredavidbelanger/registrar \
	&& export GOPATH=/go \
	&& git config --global http.https://gopkg.in.followRedirects true \
	&& go get \
	&& go build -o /usr/local/bin/registrar \
	&& rm -rf /go \
	&& apk del --purge build-deps
