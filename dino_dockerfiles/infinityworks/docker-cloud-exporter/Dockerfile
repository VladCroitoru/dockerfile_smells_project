FROM gliderlabs/alpine:3.4
MAINTAINER infinityworksltd

EXPOSE 9174

RUN addgroup exporter \
 && adduser -S -G exporter exporter

COPY . /go/src/github.com/infinityworks/docker-cloud-exporter

RUN apk --update add ca-certificates \
 && apk --update add --virtual build-deps go git \
 && cd /go/src/github.com/infinityworks/docker-cloud-exporter \
 && GOPATH=/go go get \
 && GOPATH=/go go build -o /bin/cloud_exporter \
 && apk del --purge build-deps \
 && rm -rf /go/bin /go/pkg /var/cache/apk/*

USER exporter

ENTRYPOINT [ "/bin/cloud_exporter" ]
