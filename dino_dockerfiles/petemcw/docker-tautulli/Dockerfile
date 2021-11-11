FROM lsiobase/alpine.python:3.7

# environment
ARG VERSION=v2.0.7-beta

# packages & configure
RUN apk add --update --no-cache --virtual=build-dependencies \
        g++ gcc git make python2-dev && \
    VERSIONCHECK=$(git ls-remote --tags https://github.com/JonnyWong16/plexpy.git ${VERSION} | wc -l) && \
    if [ ${VERSIONCHECK} = 0 ]; then \
        echo "Bad tag, ${VERSION}" && \
        exit 1; \
    else \
        git clone --branch ${VERSION} https://github.com/JonnyWong16/plexpy.git /app/plexpy; \
    fi && \
    apk del --purge build-dependencies && \
    rm -rf /var/cache/apk/* /tmp/* /var/tmp/*

# copy root filesystem
COPY rootfs /

# external
EXPOSE 8181
VOLUME ["/config", "/logs"]
