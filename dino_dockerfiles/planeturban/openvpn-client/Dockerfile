FROM alpine
MAINTAINER David Personette <dperson@gmail.com>


ENV VPNUSER "changeme"
ENV VPNPASS "changeme"

# Install openvpn
RUN apk --no-cache --no-progress upgrade && \
    apk --no-cache --no-progress add bash curl ip6tables iptables openvpn \
                shadow tini && \
    addgroup -S vpn && \
    rm -rf /tmp/*

COPY openvpn.sh /usr/bin/
ADD vpn /vpn
#CMD echo $VPNUSER > /vpn/auth.txt && echo $VPNPASS >> /vpn/auth.txt && chmod 700 /vpn/auth.txt

HEALTHCHECK --interval=60s --timeout=15s --start-period=120s \
             CMD curl -L 'https://api.ipify.org'

#VOLUME ["/vpn"]

ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/openvpn.sh"]
