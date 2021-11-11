FROM alpine:3.7 AS wget

ARG urldeb=https://github.com/liske/najabo/releases/download/v0.6.4/najabo_0.6.4_all.deb

WORKDIR /

RUN wget -O /najabo.deb $urldeb


FROM debian:stretch-slim

ENV NBUID 1001
ENV NBGID 1001

COPY --from=wget /najabo.deb /tmp/najabo.deb
ADD entrypoint.sh /
ADD najabo.conf.docker /etc/najabo.dist/najabo.conf
ADD najabo.vcard /etc/najabo.dist/najabo.vcard

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
    libnet-dns-perl libnet-xmpp-perl liblinux-inotify2-perl liblog-dispatch-perl \
    libproc-daemon-perl libproc-pid-file-perl libnagios-object-perl ca-certificates && \
    dpkg -i /tmp/najabo.deb && \
    mkdir -p /var/run/najabo /var/spool/najabo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/sbin/najabod", "-f", "-c", "/etc/najabo/najabo.conf"]
