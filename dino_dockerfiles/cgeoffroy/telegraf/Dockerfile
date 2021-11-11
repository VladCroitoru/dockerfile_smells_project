FROM alpine:latest

RUN apk update \
    && export ALPINE_GLIBC_URL="https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/" \
    && export GLIBC_PKG="glibc-2.21-r2.apk" \
    && export GLIBC_BIN_PKG="glibc-bin-2.21-r2.apk" \
    && apk add openssl \
    && cd /tmp \
    && wget ${ALPINE_GLIBC_URL}${GLIBC_PKG} ${ALPINE_GLIBC_URL}${GLIBC_BIN_PKG} \
    && apk add --allow-untrusted ${GLIBC_PKG} ${GLIBC_BIN_PKG} \
    && /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib \
    && echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf \
    && rm /tmp/* /var/cache/apk/*

RUN wget -c -P /tmp http://get.influxdb.org/telegraf/telegraf-0.10.1-1_linux_amd64.tar.gz \
    && tar -C /tmp -xzvf /tmp/telegraf-*linux_amd64.tar.gz \
    && mv /tmp/usr/bin/telegraf /usr/local/bin \
    && rm -rf /tmp/*

ENV HOST_PROC='/proc' HOST_SYS='/sys'

ENTRYPOINT ["/usr/local/bin/telegraf"]

CMD ["--help"]


