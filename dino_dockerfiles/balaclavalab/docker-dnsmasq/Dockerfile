FROM alpine:3.11

RUN apk add --no-cache dnsmasq

EXPOSE 53/udp

ENTRYPOINT ["/usr/sbin/dnsmasq", "-d", "-f", "-D", "-N", "--user=root"]
