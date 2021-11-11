FROM golang:1.9-alpine

ENV PROJECT_PATH github.com/linki/armor-ingress-controller

COPY . /go/src/${PROJECT_PATH}

RUN apk -U add git && \
    go get github.com/Masterminds/glide && \
    cd /go/src/${PROJECT_PATH} && \
    glide install --strip-vendor && \
    go install -v ${PROJECT_PATH}

ENTRYPOINT ["/go/bin/armor-ingress-controller"]
