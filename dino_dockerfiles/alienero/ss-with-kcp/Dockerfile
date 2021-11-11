FROM golang:alpine
MAINTAINER Yim <yiyan.lu@me.com>
ENV MODE fast2
ENV PASSWORD 123
ADD run.sh /usr/local/run.sh
RUN chmod +x /usr/local/run.sh
RUN apk update && \
    apk upgrade && \
    apk add git
RUN go get github.com/xtaci/kcptun/client && go get github.com/xtaci/kcptun/server
RUN go get github.com/shadowsocks/shadowsocks-go/cmd/shadowsocks-server
# for kcp server
EXPOSE 29900/udp 
# for shadowsocks
EXPOSE 8888 
CMD /usr/local/run.sh
