
FROM alpine:edge

RUN apk --update --no-cache add pptpd ppp iptables && \
    rm -rf /var/cache/apk/* && \
    echo 'option /etc/ppp/pptpd-options' > /etc/pptpd.conf && \
    echo 'pidfile /var/run/pptpd.pid' >> /etc/pptpd.conf && \
    echo 'localip 192.168.127.1' >> /etc/pptpd.conf && \
    echo 'remoteip 192.168.127.100-199' >> /etc/pptpd.conf && \
    echo 'name pptpd' > /etc/ppp/pptpd-options && \
    echo 'refuse-pap' >> /etc/ppp/pptpd-options && \
    echo 'refuse-chap' >> /etc/ppp/pptpd-options && \
    echo 'refuse-mschap' >> /etc/ppp/pptpd-options && \
    echo 'require-mschap-v2' >> /etc/ppp/pptpd-options && \
    echo 'require-mppe-128' >> /etc/ppp/pptpd-options && \
    echo 'proxyarp' >> /etc/ppp/pptpd-options && \
    echo 'nodefaultroute' >> /etc/ppp/pptpd-options && \
    echo 'lock' >> /etc/ppp/pptpd-options && \
    echo 'nobsdcomp' >> /etc/ppp/pptpd-options && \
    echo 'novj' >> /etc/ppp/pptpd-options && \
    echo 'novjccomp' >> /etc/ppp/pptpd-options && \
    echo 'nologfd' >> /etc/ppp/pptpd-options && \
    echo 'silent' >> /etc/ppp/pptpd-options

EXPOSE 1723/tcp
 
CMD set -ex && \
    iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE && \
    if [[ "$LOCALDNS" -eq "1" ]]; then \
        echo 'ms-dns 127.0.0.1' >> /etc/ppp/pptpd-options && \
        echo 'nameserver 127.0.0.1' > /etc/resolv.conf ; \
    else \
        echo -e 'ms-dns 8.8.8.8\nms-dns 223.5.5.5' >> /etc/ppp/pptpd-options && \
        echo -e 'nameserver 8.8.8.8\nameserver 223.5.5.5' > /etc/resolv.conf; \
    fi && \
    pptpd && \
    syslogd -n -O /dev/stdout  
