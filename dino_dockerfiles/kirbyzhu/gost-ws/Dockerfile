FROM golang:alpine

RUN apk add --update git && \
    git clone -b master https://github.com/ginuerzh/gost/ /go/src/github.com/ginuerzh/gost && \
    cd /go/src/github.com/ginuerzh/gost/cmd/gost && \
    go get ./... && go install github.com/ginuerzh/gost/cmd/gost
    
ENV MODE=ws CERT_PEM=none KEY_PEM=none

ADD entrypoint.sh /entrypoint.sh

RUN chgrp -R 0 /go/bin \
    && chmod -R g+rwX /go/bin \
    && chmod +x /entrypoint.sh 

ENTRYPOINT  /entrypoint.sh 

EXPOSE 8080
