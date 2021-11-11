FROM golang:alpine as build
MAINTAINER bartosz.gadzala@gmail.com
LABEL maintainer "bartosz.gadzala@gmail.com"
ENV LOGSPOUT_VERSION=3.2.3
ENV LOGSPOUT_DOWNLOAD_SHA256=be5a0b6c6805deb9e1dcc096409e2a0cf9302e1f25b7a163e25e25fd04e4a02d
RUN mkdir -p /go/src
WORKDIR /go/src
VOLUME /mnt/routes
EXPOSE 80

RUN apk --no-cache add curl git gcc musl-dev
RUN curl -fSL -o logspout.tar.gz "https://github.com/gliderlabs/logspout/archive/v${LOGSPOUT_VERSION}.tar.gz" \
    && echo "$LOGSPOUT_DOWNLOAD_SHA256 *logspout.tar.gz" | sha256sum -c - \
    && tar -zxvf logspout.tar.gz \
    && rm logspout.tar.gz \
    && mkdir -p /go/src/github.com/gliderlabs/ \
    && mv logspout-${LOGSPOUT_VERSION} /go/src/github.com/gliderlabs/logspout

ADD modules.go /go/src/github.com/gliderlabs/logspout/modules.go
WORKDIR /go/src/github.com/gliderlabs/logspout
RUN go get -d -v ./...
RUN go build -v -ldflags "-X main.Version=$(cat VERSION)" -o ./bin/logspout

FROM alpine:latest
COPY --from=build /go/src/github.com/gliderlabs/logspout/bin/logspout /go/bin/logspout
ENTRYPOINT ["/go/bin/logspout"]
