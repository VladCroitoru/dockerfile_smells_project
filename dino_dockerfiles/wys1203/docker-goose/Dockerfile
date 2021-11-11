FROM golang:alpine AS build-env

RUN set -ex \
        && apk add --no-cache --virtual build-dependencies \
            build-base \
            git \
        && go get -ldflags "-extldflags -static" bitbucket.org/liamstask/goose/cmd/goose \
        && apk del build-dependencies

FROM alpine

COPY --from=build-env /go/bin/goose /usr/local/bin/goose

ENTRYPOINT ["/usr/local/bin/goose"]
CMD ["--help"]
