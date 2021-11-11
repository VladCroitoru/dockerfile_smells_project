FROM golang:1.13.0-alpine3.10

RUN apk add --no-cache git upx \
    && go get -u -ldflags "-s -w" github.com/pwaller/goupx \
    && go get -u -ldflags "-s -w" github.com/lucianjon/zk-exporter \
    && goupx bin/zk-exporter


FROM alpine:3.10

COPY --from=0 /go/bin/zk-exporter /bin/zk-exporter

EXPOSE 9120

ENTRYPOINT ["/bin/zk-exporter"]

CMD ["-help"]

