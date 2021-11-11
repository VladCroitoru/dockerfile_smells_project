FROM golang:alpine

WORKDIR /go/src/github.com/svenmueller/nube
ADD . /go/src/github.com/svenmueller/nube

RUN go install && \
rm -rf /go/pkg && rm -rf /go/src && rm -rf /var/cache/apk/*

ENTRYPOINT ["nube"]
