FROM alpine:3.5

ENV GOPATH /go
ENV PATH $PATH:$GOPATH/bin
ENV CGO_ENABLED 0

WORKDIR /go/src/github.com/hackintoshrao/

RUN  \
     apk add --no-cache ca-certificates bind-tools jq bash curl && \
     apk add --no-cache --virtual .build-deps git go musl-dev && \
     go get -v -d github.com/hackintoshrao/minio && \
     go get -v -d github.com/minio/minio && \
     cd /go/src/github.com/hackintoshrao/minio && \
     go install -v -ldflags "$(go run buildscripts/gen-ldflags.go)" && \
     rm -rf /go/pkg /go/src /usr/local/go && apk del .build-deps

EXPOSE 9000

COPY buildscripts/docker-entrypoint.sh /usr/bin/

RUN chmod +x /usr/bin/docker-entrypoint.sh
RUN chmod +x /go/src/github.com/hackintoshrao/minio/minio-dcos-wrapper.sh 

ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]

VOLUME ["/export"]

CMD ["minio"]
