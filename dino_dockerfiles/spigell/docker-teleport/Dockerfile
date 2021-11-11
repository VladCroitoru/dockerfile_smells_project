FROM golang:alpine as builder
RUN apk --no-cache add git make gcc

WORKDIR /go/teleport

RUN git clone https://github.com/vadv/teleport .

RUN make submodule_check
RUN make


FROM alpine:latest
RUN apk --no-cache add ca-certificates bash
WORKDIR /root/
COPY --from=builder /go/teleport/bin/teleport .
COPY entrypoint.sh /tmp/entrypoint.sh

ENTRYPOINT ["/tmp/entrypoint.sh"]
