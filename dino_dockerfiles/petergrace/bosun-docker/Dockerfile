FROM janeczku/alpine-kubernetes:3.2

#Alpine doesn't have the glibc package, so go binaries don't behave properly.  Borrow Prometheus's build process that installs glibc.
ENV \
    ALPINE_GLIBC_URL="https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/" \
    GLIBC_PKG="glibc-2.21-r2.apk" \
    GLIBC_BIN_PKG="glibc-bin-2.21-r2.apk" \
    BOSUN_VERSION="0.5.0-rc3"

RUN \
    apk add --update -t deps wget ca-certificates openssl \
    && apk add --update -t openssl \
    && cd /tmp \
    && wget --no-check-certificate ${ALPINE_GLIBC_URL}${GLIBC_PKG} ${ALPINE_GLIBC_URL}${GLIBC_BIN_PKG} \
    && apk add --allow-untrusted ${GLIBC_PKG} ${GLIBC_BIN_PKG} \
    && /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib \
    && echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf \
    && apk del --purge deps \
    && rm /tmp/* /var/cache/apk/*


#Install bosun
RUN apk-install bash
RUN mkdir -p /opt/bosun /opt/bosun/data /etc/services.d/bosun
ADD https://github.com/bosun-monitor/bosun/releases/download/${BOSUN_VERSION}/bosun-linux-amd64 /opt/bosun/bosun
RUN chmod a+x /opt/bosun/bosun
ADD bosun/bosun.conf.sample /opt/bosun/
ADD bosun/run /etc/services.d/bosun/run

VOLUME /opt/bosun/data
EXPOSE 8070
