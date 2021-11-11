FROM golang:1.10-alpine3.7

RUN apk add -U ca-certificates curl git gcc musl-dev
RUN curl -fsSL -o /usr/local/bin/dep https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 \
		&& chmod +x /usr/local/bin/dep

RUN mkdir -p $GOPATH/src/github.com/bgpat/tweet-via-searchbar
WORKDIR $GOPATH/src/github.com/bgpat/tweet-via-searchbar

COPY Gopkg.toml Gopkg.lock ./
RUN dep ensure -vendor-only -v

ADD . ./
RUN go build --ldflags '-s -w -linkmode external -extldflags -static' -o /main -v


FROM scratch
COPY --from=0 /main /main
COPY --from=0 /etc/ssl /etc/ssl
COPY templates /templates
EXPOSE 8080
ENTRYPOINT ["/main"]
