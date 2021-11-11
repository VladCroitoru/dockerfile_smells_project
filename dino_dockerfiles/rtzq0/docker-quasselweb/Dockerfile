FROM alpine
MAINTAINER Jason Ritzke <jasonritzke@4loopz.com>

# Used for TLS certificate, override at your whim
ENV COUNTRY="US" \
    STATE="California" \
    CITY="Los Angeles" \
    QUASSELWEB_HOME="/home/quasselweb" \
    QUASSELWEB_USER="quasselweb" \
    QUASSELWEB_GROUP="quasselweb"

# Stolen from https://microbadger.com/labels
# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="docker-quasselweb" \
      org.label-schema.description="very simple and light quasselweb with persistent certificates and config" \
      org.label-schema.url="https://github.com/rtzq0/docker-quasselweb" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/rtzq0/docker-quasselweb" \
      org.label-schema.vendor="Rtzq0" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

RUN apk add --update openssl nodejs git su-exec \
    && rm -rf /var/cache/apk/* \
    && adduser -S -D -h ${QUASSELWEB_HOME} -s /sbin/nologin -g ${QUASSELWEB_USER} ${QUASSELWEB_USER} \
    && addgroup -S ${QUASSELWEB_USER} \
    && addgroup ${QUASSELWEB_USER} ${QUASSELWEB_USER} \
    && su-exec ${QUASSELWEB_USER} git clone https://github.com/magne4000/quassel-webserver.git ${QUASSELWEB_HOME}/quassel-webserver \
    && cd ${QUASSELWEB_HOME}/quassel-webserver \
    && su-exec ${QUASSELWEB_USER} npm install --production \
    && su-exec ${QUASSELWEB_USER} mkdir ${QUASSELWEB_HOME}/persist

EXPOSE 64443

VOLUME ["/home/quasselweb/persist"]
COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD su-exec ${QUASSELWEB_USER} /usr/bin/node /home/quasselweb/quassel-webserver/app.js --config /home/quasselweb/persist/settings-user.js
