FROM alpine:3.6
LABEL maintainer='Peter Wu <piterwu@outlook.com>'
ENV LANG=C.UTF-8 \
    GLIBC_VERSION=2.25-r0
WORKDIR /tmp
RUN apk upgrade --update && \
    apk add --update curl ca-certificates && \
    for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION} glibc-i18n-${GLIBC_VERSION}; do curl -sSL https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done && \
    apk add --allow-untrusted /tmp/*.apk && \
    ( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true ) && \
    echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \
    apk del curl glibc-i18n ca-certificates && \
    rm -rf /tmp/* /var/cache/apk/*