FROM progrium/busybox
MAINTAINER pjpires@gmail.com

EXPOSE 80 443

# Add stuff
RUN opkg-install haproxy ca-certificates

VOLUME ["/etc/haproxy/certs"]

ADD haproxy.cfg /etc/haproxy/haproxy.cfg

CMD ["/usr/sbin/haproxy", "-db", "-f", "/etc/haproxy/haproxy.cfg"]
