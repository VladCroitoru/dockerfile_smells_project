FROM node:14-alpine@sha256:c346198378f78f8611254dce222e7e6635804e41e5203d1825321edd6c59dca1

LABEL maintainer="ownCloud DevOps <devops@owncloud.com>"
LABEL org.opencontainers.image.authors="ownCloud DevOps <devops@owncloud.com>"
LABEL org.opencontainers.image.title="Etherpad Lite"
LABEL org.opencontainers.image.url="https://github.com/owncloud-ops/etherpad"
LABEL org.opencontainers.image.source="https://github.com/owncloud-ops/etherpad"
LABEL org.opencontainers.image.documentation="https://github.com/owncloud-ops/etherpad"

ARG BUILD_VERSION
ARG ETHERPAD_PLUGINS
ARG GOMPLATE_VERSION
ARG WAIT_FOR_VERSION

# renovate: datasource=github-releases depName=ether/etherpad-lite
ENV ETHERPAD_VERSION="${BUILD_VERSION:-1.8.14}"
# renovate: datasource=github-releases depName=hairyhenderson/gomplate
ENV GOMPLATE_VERSION="${GOMPLATE_VERSION:-v3.10.0}"
# renovate: datasource=github-releases depName=thegeeklab/wait-for
ENV WAIT_FOR_VERSION="${WAIT_FOR_VERSION:-v0.2.0}"

ENV NODE_ENV=production
ENV NPM_CONFIG_LOGLEVEL=error

ADD overlay /
WORKDIR /opt/app

RUN apk --update --no-cache add libreoffice tidyhtml

RUN addgroup -g 1001 -S app && \
    adduser -S -D -H -u 1001 -h /opt/app -s /sbin/nologin -G app -g app app

RUN apk --update add --virtual .build-deps curl tar git make && \
    curl -SsL -o /usr/local/bin/gomplate "https://github.com/hairyhenderson/gomplate/releases/download/${GOMPLATE_VERSION}/gomplate_linux-amd64-slim" && \
    curl -SsL -o /usr/local/bin/wait-for "https://github.com/thegeeklab/wait-for/releases/download/${WAIT_FOR_VERSION}/wait-for" && \
    chmod 755 /usr/local/bin/gomplate && \
    chmod 755 /usr/local/bin/wait-for && \
    mkdir -p /opt/app/node_modules && \
    # workaround to get rid of some startup warnings
    mkdir -p /opt/app/.git && \
    echo "xxxxxpseudo" > /opt/app/.git/HEAD && \
    touch /opt/app/.git/pseudo && \
    ETHERPAD_VERSION="${ETHERPAD_VERSION##v}" && \
    echo "Installing Etherpad version '${ETHERPAD_VERSION}' ..." && \
    curl -SsL "https://github.com/ether/etherpad-lite/archive/${ETHERPAD_VERSION}.tar.gz" | \
        tar xz -C /opt/app -X /.tarignore --strip-components=1 && \
    cd /opt/app/node_modules && \
    ln -s ../src ep_etherpad-lite && \
    cd /opt/app/src/ && \
    npm ci --no-optional && \
    cd /opt/app/ && \
    for PLUGIN in ${ETHERPAD_PLUGINS}; do npm i "${PLUGIN}" || exit 1; done && \
    chown -R app:app /opt/app && \
    apk del .build-deps && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*

EXPOSE 9001

USER app

ENTRYPOINT ["/usr/bin/entrypoint"]
CMD []
