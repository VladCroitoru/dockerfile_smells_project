FROM golang:alpine AS builder
RUN apk update && apk add --no-cache git
WORKDIR /go/src/v2ray.com/core
RUN git clone --progress https://github.com/v2fly/v2ray-core.git . && \
    go mod download && \
    CGO_ENABLED=0 go build -o /tmp/v2ray -trimpath -ldflags "-s -w -buildid=" ./main

FROM alpine
COPY --from=builder /tmp/v2ray /usr/bin

ADD v2ray.sh /v2ray.sh
RUN chmod +x /v2ray.sh
CMD /v2ray.sh
