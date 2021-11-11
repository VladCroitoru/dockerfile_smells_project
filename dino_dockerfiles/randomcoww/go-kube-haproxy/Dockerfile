FROM golang:alpine as BUILD

WORKDIR /go/src/goapp/
COPY . .

RUN set -x \
  \
  && apk add --no-cache \
    git \
  \
  && go get -d ./... \
  && go build

FROM alpine:edge

COPY --from=BUILD /go/src/goapp/goapp /

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
