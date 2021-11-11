FROM golang:alpine
MAINTAINER Jean-François Roche <jfroche@affinitic.be>
EXPOSE 53/udp 53/tcp
ADD . /go/src/puppetdb-dns
RUN apk add --update git && \
    go get -v puppetdb-dns && \
    go build -o puppetdb-dns puppetdb-dns && \
    apk del git go && \
    rm -rf /go/pkg && \
    rm -rf /go/src && \
    rm -rf /var/cache/apk/*
CMD ["/go/bin/puppetdb-dns"]
