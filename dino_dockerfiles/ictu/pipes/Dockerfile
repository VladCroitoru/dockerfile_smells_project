FROM alpine:3.6

ENV IF_NAME eth0
ENV NET_PREFIX "10\."
ENV DNSREG_SOCKET /var/run/dnsreg/dnsreg.sock

ADD entrypoint.sh /entrypoint.sh
ADD hooks/05-bound /usr/lib/dhcpcd/dhcpcd-hooks/05-bound

RUN apk --no-cache add tini dhcpcd netcat-openbsd && \
    chmod +x /entrypoint.sh && \
    echo "nohook resolv.conf" >> /etc/dhcpcd.conf

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]
