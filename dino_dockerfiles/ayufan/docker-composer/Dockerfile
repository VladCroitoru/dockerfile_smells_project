FROM golang:alpine as build
COPY . $GOPATH/src/github.com/ayufan/docker-composer/
RUN go install -v github.com/ayufan/docker-composer

FROM docker/compose:1.22.0

RUN apk add -U git docker && \
  git config --global receive.denyCurrentBranch updateInstead && \
  git config --global user.name Composer && \
  git config --global user.email you@example.com

ENV APPS_DIR=/srv/apps \
  GOPATH=/go

COPY --from=0 /go/bin/docker-composer /usr/bin/composer
VOLUME ["/srv/apps"]
ADD examples/ /srv/apps/

ENTRYPOINT ["/usr/bin/composer"]
