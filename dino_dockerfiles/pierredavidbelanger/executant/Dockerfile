FROM alpine:3.7
ENTRYPOINT ["/usr/local/bin/executant"]

COPY . /go/src/github.com/pierredavidbelanger/executant
RUN apk --no-cache add -t build-deps build-base go git \
	&& apk --no-cache add ca-certificates py-pip \
	&& pip install docker-compose \
	&& cd /go/src/github.com/pierredavidbelanger/executant \
	&& export GOPATH=/go \
	&& git config --global http.https://gopkg.in.followRedirects true \
	&& go get \
	&& go build -o /usr/local/bin/executant \
	&& rm -rf /go \
	&& apk del --purge build-deps
