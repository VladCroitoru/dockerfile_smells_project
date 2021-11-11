FROM golang:1.6-alpine

RUN apk add libvips-dev ca-certificates --no-cache --repository https://s3.amazonaws.com/wjordan-apk --allow-untrusted

ADD . /go/src/github.com/monder/wain/

RUN apk add --no-cache git build-base && \
    go get github.com/Masterminds/glide && \
    cd /go/src/github.com/monder/wain/ && \
    glide install && \
    go install && \
    rm -rf /go/src && \
    apk del build-base git

ENTRYPOINT ["wain"]
