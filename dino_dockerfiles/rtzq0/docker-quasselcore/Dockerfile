FROM alpine
MAINTAINER Jason Ritzke <jasonritzke@4loopz.com>

# Used for TLS certificate, override at your whim
ENV COUNTRY="US" \
    STATE="California" \
    CITY="Los Angeles" \
    QUASSEL_HOME="/var/lib/quassel" \
    QUASSEL_USER="quassel" \
    QUASSEL_GROUP="quassel" \
    QUASSEL_CERT="/var/lib/quassel/quasselCert.pem"

# Stolen from https://microbadger.com/labels          
# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="docker-quasselcore" \
      org.label-schema.description="very simple and light quasselcore with persistent storage" \
      org.label-schema.url="https://github.com/rtzq0/docker-quasselcore" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/rtzq0/docker-quasselcore" \
      org.label-schema.vendor="Rtzq0" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

RUN apk add --update quassel-core qt-sqlite openssl su-exec\
    && rm -rf /var/cache/apk/*

EXPOSE 4242

VOLUME ["/var/lib/quassel"]
COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD su-exec ${QUASSEL_USER} /usr/bin/quasselcore --configdir=${QUASSEL_HOME}
