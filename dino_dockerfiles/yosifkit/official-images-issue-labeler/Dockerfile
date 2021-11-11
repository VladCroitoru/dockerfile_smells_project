FROM golang:1.8

RUN go get -d -v \
		github.com/google/go-github/github \
		github.com/jessevdk/go-flags \
		golang.org/x/net/context \
		golang.org/x/oauth2

WORKDIR /go/src/app
COPY *.go ./

RUN set -x \
	&& go install -v ./... \
	&& ! app \
	&& ! app bogus \
	&& ! app --bogus \
	&& ! app --token bogus bogus \
	&& ! app --token bogus --bogus \
	&& app --help \
	&& app -h

ENTRYPOINT ["app"]
