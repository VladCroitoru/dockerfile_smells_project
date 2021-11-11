FROM golang:1.7.1-alpine
RUN apk --update add git && \
    go get github.com/wowlusitong/shadowsocks-go/cmd/shadowsocks-server
COPY config.json /config.json
ENTRYPOINT ["shadowsocks-server"]
