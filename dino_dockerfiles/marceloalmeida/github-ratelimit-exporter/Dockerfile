FROM alpine

EXPOSE 8080

RUN set -ex \
    && export GOPATH=/tmp/go \
    && apk add --update --no-cache --virtual .build-deps \
        git \
        go \
        build-base \
    && cd /tmp \
    && git config --global http.https://gopkg.in.followRedirects true \
    && go get gopkg.in/tylerb/graceful.v1 \
    && { go get -d github.com/marceloalmeida/github-ratelimit-exporter ; : ; } \
    && cd $GOPATH/src/github.com/marceloalmeida/github-ratelimit-exporter \
    && go build -o /bin/github-ratelimit-exporter main.go \
    && apk del .build-deps \
    && rm -rf /tmp/* /root/.gitconfig \
    && apk --update --no-cache add ca-certificates

ENTRYPOINT ["/bin/github-ratelimit-exporter"]
