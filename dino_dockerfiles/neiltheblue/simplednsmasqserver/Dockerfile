FROM alpine:3.4

RUN apk --no-cache add dnsmasq syslinux
RUN mkdir /pxeboot && \
cp /usr/share/syslinux/ldlinux.c32 /pxeboot && \
cp /usr/share/syslinux/libcom32.c32 /pxeboot && \
cp /usr/share/syslinux/libutil.c32 /pxeboot && \
cp /usr/share/syslinux/vesamenu.c32 /pxeboot && \
cp /usr/share/syslinux/lpxelinux.0 /pxeboot && \
cp /usr/share/syslinux/memdisk /pxeboot && mkdir /pxeboot/pxelinux.cfg

COPY entrypoint.sh /entrypoint.sh

EXPOSE 53 53/udp

ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]
