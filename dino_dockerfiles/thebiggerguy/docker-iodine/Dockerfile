FROM alpine:edge
MAINTAINER Guy Taylor <thebigguy.co.uk@gmail.com>

RUN apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ iodine tini iptables && \
    echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf && \
    echo "net.ipv6.conf.all.forwarding = 1" >> /etc/sysctl.conf

RUN mkdir -p /opt/iodine
ADD start.sh /opt/iodine/start.sh

WORKDIR /opt/iodine

EXPOSE 53/udp

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["./start.sh"]
