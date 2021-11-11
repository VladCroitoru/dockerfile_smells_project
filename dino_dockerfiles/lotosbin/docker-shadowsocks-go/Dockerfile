FROM debian:latest
MAINTAINER lotosbin <lotosbin@gmail.com>
ADD https://github.com/shadowsocks/shadowsocks-go/releases/download/1.1.5/shadowsocks-server-linux64-1.1.5.gz /etc/ss-server.gz
RUN gunzip /etc/ss-server.gz
RUN chmod +x /etc/ss-server

ENTRYPOINT ["/etc/ss-server"]
