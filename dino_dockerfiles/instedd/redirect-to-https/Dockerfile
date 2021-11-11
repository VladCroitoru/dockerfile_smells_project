FROM alpine:3.5

RUN \
  apk add --update haproxy && \
  rm -rf /var/cache/apk/*

ADD haproxy.cfg /etc/haproxy/haproxy.cfg

EXPOSE 80
CMD ["/usr/sbin/haproxy", "-f", "/etc/haproxy/haproxy.cfg"]
