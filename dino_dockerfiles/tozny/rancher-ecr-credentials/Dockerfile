FROM golang:alpine3.6

COPY . /go/src/rancher-ecr-credentials/
WORKDIR /go/src/rancher-ecr-credentials/

RUN apk add --no-cache git \
    && go get github.com/kardianos/govendor \
    && mkdir -p /go/src/rancher-ecr-credentials \
    && GOOS=linux GOARCH=amd64 CGO_ENABLED=0 govendor build -a -installsuffix cgo \
    && mv rancher-ecr-credentials /bin/ \
    && rm -rf /go/src/rancher-ecr-credentials

ENTRYPOINT ["/bin/rancher-ecr-credentials"]
