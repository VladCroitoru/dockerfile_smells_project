FROM scratch

ARG BUILD_DATE
ARG ALPINE_RELEASE
ARG ALPINE_VERSION
ARG ALPINE_VERSION_DATE

# set our environment variable
ENV MUSL_LOCPATH="/usr/share/i18n/locales/musl"

LABEL maintainer="Mauro Cardillo <mauro.cardillo@gmail.com>" \
    architecture="amd64/x86_64" \
    alpine-version="$ALPINE_VERSION" \
    build="$BUILD_DATE" \
    org.opencontainers.image.title="alpine" \
    org.opencontainers.image.description="Docker image running on Alpine Linux" \
    org.opencontainers.image.authors="Mauro Cardillo <mauro.cardillo@gmail.com>" \
    org.opencontainers.image.vendor="Mauro Cardillo" \
    org.opencontainers.image.version="v$ALPINE_VERSION" \
    org.opencontainers.image.url="https://hub.docker.com/r/maurosoft1973/alpine/" \
    org.opencontainers.image.source="https://gitlab.com/maurosoft1973-docker/alpine" \
    org.opencontainers.image.created=$BUILD_DATE

ADD alpine-$ALPINE_VERSION/amd64/alpine-minirootfs-$ALPINE_VERSION-x86_64.tar.gz /

RUN apk --no-cache add libintl tzdata && \
    apk --no-cache add musl-locales --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing && \
    apk add tzdata && \
    mkdir /scripts

COPY files /scripts/

RUN chmod -R 755 /scripts

ENTRYPOINT ["/scripts/run-alpine.sh"]
