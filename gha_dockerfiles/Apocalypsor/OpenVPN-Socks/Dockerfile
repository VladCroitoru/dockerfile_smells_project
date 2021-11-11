FROM alpine

COPY sockd.sh /usr/local/bin/

RUN apk add --update-cache dante-server openvpn bash openresolv openrc \
    && rm -rf /var/cache/apk/* \
    && chmod a+x /usr/local/bin/sockd.sh

COPY sockd.conf /etc/

ENTRYPOINT [ \
    "/bin/bash", "-c", \
    "cd /etc/openvpn && /usr/sbin/openvpn --config *.conf --script-security 2 --up /usr/local/bin/sockd.sh" \
    ]
