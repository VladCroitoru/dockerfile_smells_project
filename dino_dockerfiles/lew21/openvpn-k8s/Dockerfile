FROM alpine:3.4

RUN apk --no-cache add openvpn iptables

EXPOSE 1194/tcp
EXPOSE 1194/udp

WORKDIR /etc/openvpn
RUN rm /etc/openvpn/*

ADD run.sh /usr/local/bin/run.sh
CMD ["/bin/sh", "/usr/local/bin/run.sh"]
