FROM node:9 as node-builder

COPY . /redalert

WORKDIR /redalert

RUN make build-ui

FROM golang:1.10 as go-builder

RUN apt-get update && \
    apt-get install ca-certificates

COPY --from=node-builder /redalert /go/src/github.com/jonog/redalert

RUN curl https://glide.sh/get | sh

WORKDIR /go/src/github.com/jonog/redalert

ENV CGO_ENABLED=0 \
    GODEBUG=netdns=go

RUN make install-deps && \
    make build

FROM scratch

COPY --from=go-builder /go/src/github.com/jonog/redalert/redalert /redalert
COPY --from=go-builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

EXPOSE 8888

ENTRYPOINT ["/redalert"]
CMD ["server"]
