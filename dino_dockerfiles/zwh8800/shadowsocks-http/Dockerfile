FROM golang:1.6.2-alpine
MAINTAINER zwh8800 <496781108@qq.com>

WORKDIR /work

RUN apk update && apk add build-base openssl ca-certificates git tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    go get github.com/shadowsocks/shadowsocks-go/cmd/shadowsocks-local && \
    wget https://github.com/jech/polipo/archive/master.zip -O polipo.zip && \
    unzip polipo.zip && \
    cd polipo-master && \
    make && \
    install polipo /usr/local/bin/ && \
    cd .. && \
    rm -rf polipo.zip polipo-master && \
    mkdir -p /usr/share/polipo/www /var/cache/polipo && \
    apk del build-base openssl && \
    rm -rf /var/cache/apk/*

ADD start.sh /work

VOLUME /etc/shadowsocks

EXPOSE 8123

CMD ["./start.sh"]
