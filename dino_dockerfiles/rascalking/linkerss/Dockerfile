FROM golang:1.6-alpine
RUN apk add --update git && rm -rf /var/cache/apk/*
ADD . /go/src/github.com/rascalking/linkerss
RUN go get -d -v \
	github.com/coreos/pkg/flagutil \
	github.com/dghubble/go-twitter/twitter \
	github.com/garyburd/redigo/redis \
	github.com/gorilla/feeds \
	golang.org/x/oauth2 \
	golang.org/x/net/html
RUN go install -v github.com/rascalking/linkerss/linkerss
ENTRYPOINT ["/go/bin/linkerss"]
EXPOSE 9999
