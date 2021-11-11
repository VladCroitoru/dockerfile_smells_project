
FROM alpine:3.6

MAINTAINER Bodo Schulz <bodo@boone-schulz.de>

ENV \
  ALPINE_MIRROR="mirror1.hs-esslingen.de/pub/Mirrors" \
  ALPINE_VERSION="v3.6" \
  TERM=xterm \
  BUILD_DATE="2017-07-13" \
  VERSION="3.4.4"

EXPOSE 27017 27018 27019 28017

LABEL \
  version="1707-28.1" \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.name="Mongodb Docker Image" \
  org.label-schema.description="Inofficial Mongodb Docker Image" \
  org.label-schema.url="FILL_ME" \
  org.label-schema.vcs-url="https://github.com/bodsch/docker-mongodb" \
  org.label-schema.vendor="Bodo Schulz" \
  org.label-schema.version=${VERSION} \
  org.label-schema.schema-version="1.0" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="The Unlicense"

# ---------------------------------------------------------------------------------------

RUN \
  echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/main"       > /etc/apk/repositories && \
  echo "http://${ALPINE_MIRROR}/alpine/${ALPINE_VERSION}/community" >> /etc/apk/repositories && \
  apk --no-cache update && \
  apk --no-cache upgrade && \
  apk --no-cache add \
    mongodb && \
  mkdir -vp /data/db && \
  rm -rf \
    /tmp/* \
    /var/cache/apk/*

VOLUME [ "/data" ]

ENTRYPOINT [ "mongod" ]

CMD [ "--smallfiles", "--oplogSize", "128" , "--replSet", "rs0" ]

# EOF
