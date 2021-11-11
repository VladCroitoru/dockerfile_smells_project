FROM golang:alpine
MAINTAINER 178inaba <178inaba@users.noreply.github.com>

ENV INSTALL_PKG git
RUN apk update && apk add --no-cache $INSTALL_PKG || \
    (sed -i -e s/dl-cdn/dl-4/g /etc/apk/repositories && apk update && apk add --no-cache $INSTALL_PKG) && \
    rm -frv /var/cache/apk/*

WORKDIR /go/src/github.com/178inaba/fizzbuzz-twitterbot
COPY . .
RUN go get -d -v
RUN go install -v -tags docker

CMD ["fizzbuzz-twitterbot"]
