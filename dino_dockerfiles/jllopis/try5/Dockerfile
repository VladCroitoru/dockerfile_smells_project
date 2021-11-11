FROM golang:1.4.2-wheezy

ENV APP github.com/jllopis/try5
ADD . /go/src/${APP}
WORKDIR /go/src/${APP}
RUN go get github.com/tools/godep \
    && godep go install ${APP}/cmd/try5d \
    && mkdir /var/lib/try5

VOLUME ["/var/lib/try5", "/etc/try5d/certs"]

EXPOSE 9000
ENTRYPOINT /go/bin/try5d
