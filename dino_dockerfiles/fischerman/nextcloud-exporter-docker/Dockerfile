FROM golang:1.9.2 AS go
RUN go get github.com/xperimental/nextcloud-exporter

ENTRYPOINT ["/go/bin/nextcloud-exporter"]