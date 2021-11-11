FROM alpine:3.4

ADD https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 /usr/bin/confd
RUN chmod +x /usr/bin/confd && mkdir -p /etc/confd

ADD ./conf.d /etc/confd/conf.d
ADD ./templates /etc/confd/templates

ENTRYPOINT ["/usr/bin/confd"]
CMD ["--backend", "rancher", "--prefix", "/2015-07-25", "--node", "rancher-metadata.rancher.internal", "--log-level", "debug"]
