# Dockerfile for troglobit's inadyn
#
# See: http://troglobit.com/inadyn.html
#      https://github.com/troglobit/inadyn/releases
#      https://github.com/troglobit/libite/releases
#      https://github.com/martinh/libconfuse/releases
#
# Run inadyn with strace if it exits without any error
#

FROM alpine:edge

ENV INADYN_RELEASE https://github.com/troglobit/inadyn/releases/download/v2.2.1/inadyn-2.2.1.tar.xz
ENV LIBITE_RELEASE https://github.com/troglobit/libite/releases/download/v2.0.1/libite-2.0.1.tar.xz
ENV LIBCONFUSE_RELEASE https://github.com/martinh/libconfuse/releases/download/v3.2.1/confuse-3.2.1.tar.xz

RUN apk --update add curl xz build-base libressl-dev ca-certificates && \
    mkdir -p /tmp/src/libite /tmp/src/libconfuse /tmp/src/inadyn && \
    # Libite
    curl -Lo /tmp/src/libite.tar.xz $LIBITE_RELEASE && \
    tar --strip-components=1 -C /tmp/src/libite -xJf /tmp/src/libite.tar.xz && \
    cd /tmp/src/libite && \
    ./configure && \
    make && \
    make install && \
    # Libconfuse
    curl -Lo /tmp/src/libconfuse.tar.xz $LIBCONFUSE_RELEASE && \
    tar --strip-components=1 -C /tmp/src/libconfuse -xJf /tmp/src/libconfuse.tar.xz && \
    cd /tmp/src/libconfuse && \
    ./configure && \
    make && \
    make install && \
    # Inadyn
    curl -Lo /tmp/src/inadyn.tar.xz $INADYN_RELEASE && \
    tar --strip-components=1 -C /tmp/src/inadyn -xJf /tmp/src/inadyn.tar.xz && \
    cd /tmp/src/inadyn && \
    ./configure --enable-openssl && \
    make && \
    make install && \
    # Cleanup
    rm -rf /tmp/src && \
    apk del xz build-base && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/local/sbin/inadyn", "--foreground"]
CMD ["--loglevel=info"]
