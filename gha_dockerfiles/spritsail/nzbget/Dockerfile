FROM spritsail/alpine:3.13

ARG NZBGET_VER=21.1
ARG CXXFLAGS="-Ofast -pipe -fstack-protector-strong"
ARG LDFLAGS="-Wl,-O1,--sort-common -Wl,-s"

WORKDIR /tmp

RUN apk add --no-cache \
        unrar p7zip \
        libxml2 openssl zlib ca-certificates \
 && apk add --no-cache -t build_deps \
        jq git g++ make autoconf \
        libxml2-dev zlib-dev openssl-dev \
    \
 && git clone -b develop https://github.com/nzbget/nzbget.git . \
 && git reset "v${NZBGET_VER}" --hard \
    \
 && ./configure \
        --disable-dependency-tracking \
        --disable-curses \
 && make -j$(nproc 2>/dev/null || grep processor /proc/cpuinfo | wc -l || echo 1) \
    \
 && sed -i 's|\(^AppDir=\).*|\1/nzbget|; \
            s|\(^WebDir=\).*|\1/${AppDir}/webui|; \
            s|\(^MainDir=\).*|\1/downloads|; \
            s|\(^LogFile=\).*|\1/config/nzbget.log|; \
            s|\(^ConfigTemplate=\).*|\1/${AppDir}/nzbget.conf|; \
            s|\(^OutputMode=\).*|\1loggable|' nzbget.conf \
 && sed -i "s|\\(^UnrarCmd=\\).*|\\1$(which unrar)|; \
            s|\\(^SevenZipCmd=\\).*|\\1$(which 7z)|; \
            s|\\(^CertStore=\\).*|\\1/etc/ssl/certs/ca-certificates.crt|; \
            s|\\(^CertCheck=\\).*|\\1yes|" nzbget.conf \
 && mkdir /nzbget /downloads \
 && mv nzbget nzbget.conf webui COPYING /nzbget \
 && chmod g+rw /nzbget \
 && ln -sfv ../../nzbget/nzbget /usr/bin \
    \
 && find /tmp -mindepth 1 -delete \
 && apk del --no-cache build_deps

# ~~~~~~~~~~~~~~~~

ENV SUID=904 SGID=900
ENV NZBGET_CONF_FILE="/config/nzbget.conf"

LABEL maintainer="Spritsail <nzbget@spritsail.io>" \
      org.label-schema.name="NZBGet" \
      org.label-schema.url="https://nzbget.net/" \
      org.label-schema.description="NZBGet - the efficient Usenet downloader" \
      org.label-schema.version=${NZBGET_VER} \
      io.spritsail.version.nzbget=${NZBGET_VER}

WORKDIR /nzbget

HEALTHCHECK --start-period=5s --timeout=3s \
    CMD wget -qO- -S http://$(sed -nE 's/^ControlUsername=(.*)$/\1/p' /config/nzbget.conf):$(sed -nE 's/^ControlPassword=(.*)$/\1/p' /config/nzbget.conf)@0.0.0.0:6789/jsonrpc/version

EXPOSE 6789
VOLUME ["/config", "/downloads"]
ENTRYPOINT ["/sbin/tini", "--"]
CMD set -e; \
    if [ ! -f "$NZBGET_CONF_FILE" ]; then \
        install -m 644 -o $SUID -g $SGID /nzbget/nzbget.conf $NZBGET_CONF_FILE; \
        echo "Created default config file at $NZBGET_CONF_FILE"; \
    fi; \
    \
    su-exec -e test -w /config || chown $SUID:$SGID /config; \
    su-exec -e test -w /downloads || chown $SUID:$SGID /downloads; \
    # Ensure nzbget directory is writeable by the running user
    chgrp -R $SGID /nzbget; \
    \
    exec su-exec -e nzbget -c $NZBGET_CONF_FILE -s -o OutputMode=log

