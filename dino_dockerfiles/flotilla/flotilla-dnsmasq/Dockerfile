FROM alpine:latest
MAINTAINER Craig Tracey <craigtracey@gmail.com>

COPY docker-entrypoint.sh /bin/docker-entrypoint.sh
RUN apk update && apk add dnsmasq syslinux inotify-tools
RUN mkdir -p /var/lib/tftproot && ln -s /usr/share/syslinux /var/lib/tftproot/pxelinux
RUN wget http://boot.ipxe.org/undionly.kpxe -O /var/lib/tftproot/undionly.kpxe && \
    md5sum /var/lib/tftproot/undionly.kpxe | [ `awk '{print $1}'` == "75d9aa1ddd5a9b9382cdc6bba2515e4a" ]
RUN wget http://boot.ipxe.org/ipxe.pxe -O /var/lib/tftproot/ipxe.pxe \
    && md5sum /var/lib/tftproot/ipxe.pxe | [ `awk '{print $1}'` == "881f884bee558076b1c9b02a2feff7f8" ]

CMD ["/bin/docker-entrypoint.sh"]
