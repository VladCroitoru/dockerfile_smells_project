FROM golang:1.16-alpine as builder

RUN mkdir -p LogWatcher/bin/
WORKDIR LogWatcher/
RUN apk add --no-cache make

COPY go.mod .
COPY go.sum .
COPY Makefile .
COPY app/ ./app
COPY pkg/ ./pkg

RUN make app

FROM scratch

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /go/LogWatcher/bin/LogWatcher .
COPY config.yaml .

EXPOSE 27100/udp

ENTRYPOINT ["./LogWatcher"]
