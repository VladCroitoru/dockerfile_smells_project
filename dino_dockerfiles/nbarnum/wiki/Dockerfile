FROM golang:alpine as builder
RUN apk add --update git && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /go/src/wiki
WORKDIR /go/src/wiki
COPY . /go/src/wiki
RUN go get -d && \
    go get github.com/GeertJohan/go.rice/rice && \
    rice embed-go && \
    GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o wiki

FROM busybox
ENV WIKI_BIND=0.0.0.0:8000 \
    WIKI_BRAND=Wiki \
    WIKI_DATA=/data \
    WIKI_CONFIG=""
COPY --from=builder /go/src/wiki/wiki /wiki
VOLUME /data
EXPOSE 8000/tcp
ENTRYPOINT ["/wiki"]
