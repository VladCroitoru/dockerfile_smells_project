FROM golang:alpine

LABEL maintainer "Knut Ahlers <knut@ahlers.me>"

ADD . /go/src/github.com/Luzifer/ediplug_ctrl
WORKDIR /go/src/github.com/Luzifer/ediplug_ctrl

RUN set -ex \
 && apk add --update git ca-certificates \
 && go install -ldflags "-X main.version=$(git describe --tags || git rev-parse --short HEAD || echo dev)" \
 && apk del --purge git

EXPOSE 3000

ENTRYPOINT ["/go/bin/ediplug_ctrl"]
CMD ["--"]
