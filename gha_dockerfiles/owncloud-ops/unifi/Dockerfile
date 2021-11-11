FROM alpine:3.14@sha256:e1c082e3d3c45cccac829840a25941e679c25d438cc8412c2fa221cf1a824e6a

LABEL maintainer="ownCloud DevOps <devops@owncloud.com>"
LABEL org.opencontainers.image.authors="ownCloud DevOps <devops@owncloud.com>"
LABEL org.opencontainers.image.title="Unifi Controller"
LABEL org.opencontainers.image.url="https://github.com/owncloud-ops/unifi"
LABEL org.opencontainers.image.source="https://github.com/owncloud-ops/unifi"
LABEL org.opencontainers.image.documentation="https://github.com/owncloud-ops/unifi"

ARG BUILD_VERSION
ARG WAIT_FOR_VERSION

ENV UNIFI_VERSION="${BUILD_VERSION:-6.4.54}"
# renovate: datasource=github-releases depName=thegeeklab/wait-for
ENV WAIT_FOR_VERSION="${WAIT_FOR_VERSION:-v0.2.0}"

ENV TZ=UTC
ENV UNIFI_JVM_INIT_HEAP_SIZE=1024M

ADD overlay /

RUN apk --update --no-cache add bash ca-certificates gettext asciidoc \
    git git-lfs gnupg openssh-keygen

RUN addgroup -g 1001 -S unifi && \
    adduser -S -D -H -u 1001 -h /opt/app -s /bin/bash -G unifi -g unifi unifi

RUN apk --update add --virtual .build-deps curl libarchive-tools tar && \
    apk --update add binutils coreutils curl libcap openjdk8-jre openssl shadow su-exec tzdata gcompat && \
    curl -SsL -o /usr/local/bin/wait-for "https://github.com/thegeeklab/wait-for/releases/download/${WAIT_FOR_VERSION}/wait-for" && \
    chmod 755 /usr/local/bin/wait-for && \
    mkdir -p /opt/app/unifi/logs && \
    mkdir -p /opt/app/unifi/data && \
    mkdir -p /opt/app/unifi/run && \
    UNIFI_VERSION="${UNIFI_VERSION##v}" && \
    echo "Setup Unifi Controller 'v${UNIFI_VERSION}' ..." && \
    curl -SsL "https://www.ubnt.com/downloads/unifi/${UNIFI_VERSION}/UniFi.unix.zip" | \
        bsdtar -xf - -C /opt/app/unifi -X /.tarignore --strip-components=1 && \
    chown -R unifi:unifi /opt/app/unifi && \
    apk del .build-deps && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

VOLUME /opt/app/unifi/data

EXPOSE 3478/udp 6789/tcp 8080/tcp 8443/tcp

USER unifi

ENTRYPOINT ["/usr/bin/entrypoint"]
HEALTHCHECK --interval=10s --timeout=5s --retries=3 CMD /usr/bin/healthcheck
WORKDIR /opt/app/unifi
CMD []
