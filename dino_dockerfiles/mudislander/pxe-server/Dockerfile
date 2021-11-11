FROM alpine:3.7

RUN apk add --no-cache dnsmasq bash
COPY data/entrypoint /entrypoint
RUN chmod 755 /entrypoint

ENV DNSMASQ_HOME /mnt/dnsmasq
WORKDIR ${DNSMASQ_HOME}
EXPOSE 53/udp

ENTRYPOINT ["/entrypoint"]
CMD ["-d", "-C", "dnsmasq.conf"]
