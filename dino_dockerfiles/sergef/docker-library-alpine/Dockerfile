FROM scratch

ARG VERSION=v3.6
ENV VERSION=${VERSION}

# curl -o rootfs-edge.tar.xz https://raw.githubusercontent.com/gliderlabs/docker-alpine/rootfs/library-edge/versions/library-edge/rootfs.tar.xz OUT=rootfs-edge.tar.xz

ADD rootfs-${VERSION}.tar.xz /

# Global list of Mirrors can be found here:
# http://rsync.alpinelinux.org/alpine/MIRRORS.txt
# http://alpine.gliderlabs.com/alpine is the fastest mirror by Fastly

ARG APK_REPO=http://alpine.gliderlabs.com/alpine

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/glibc-compat/bin:/usr/glibc-compat/sbin

COPY apk.sh /apk.sh

RUN chmod +x /apk.sh \
  && /apk.sh ${APK_REPO} \
  && apk add --no-cache \
    ca-certificates \
    libgcc \
    tini@community \
  && rm -rf \
    /tmp/* \
    /var/cache/apk/*
