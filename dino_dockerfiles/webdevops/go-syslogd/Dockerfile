FROM golang:alpine AS buildenv

COPY . /go/src/go-syslogd
WORKDIR /go/src/go-syslogd

RUN apk --no-cache add git \
    && go get \
    && go build \
    && chmod +x go-syslogd \
    && ./go-syslogd --version

FROM alpine
COPY --from=buildenv /go/src/go-syslogd/go-syslogd /usr/local/bin
CMD ["go-syslogd"]
