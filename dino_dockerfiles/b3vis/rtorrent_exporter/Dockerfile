FROM golang:alpine AS build
MAINTAINER b3vis
RUN apk add alpine-sdk --no-cache && \
    go get -u github.com/mdlayher/rtorrent_exporter && \
    go get -t -v ./...

FROM alpine:latest
COPY --from=build /go/bin/rtorrent_exporter /usr/local/bin/rtorrent_exporter
EXPOSE 9135
CMD /usr/local/bin/rtorrent_exporter -rtorrent.addr $RTORRENTADDR
