FROM golang:alpine

RUN apk add --update git tzdata && rm -rf /var/cache/apk/*
RUN ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

COPY . $GOPATH/src/github.com/hacsoc/slacksoc

RUN set -x \
	&& cd $GOPATH/src/github.com/hacsoc/slacksoc \
	&& go build -o /usr/bin/slacksoc . \
	&& rm -rf $GOPATH

ADD startup.sh /usr/bin/
ADD slacksoc.yaml /etc/

CMD ["startup.sh"]
