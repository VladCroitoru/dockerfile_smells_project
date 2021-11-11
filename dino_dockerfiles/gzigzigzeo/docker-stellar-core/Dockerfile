ARG CONFD_VERSION=0.14.0
FROM gzigzigzeo/docker-download-confd as confd

# ===============================================

FROM debian:jessie AS build

ENV STELLAR_CORE_VERSION "9.0.1-475-7ad53a57"
ENV STELLAR_DEB_URL "https://s3.amazonaws.com/stellar.org/releases/stellar-core/stellar-core-${STELLAR_CORE_VERSION}_amd64.deb"

RUN apt-get update && apt-get install -y curl git libpq-dev libsqlite3-dev libsasl2-dev postgresql-client vim zlib1g-dev && apt-get clean

# Installation
RUN curl -f -L -o stellar-core.deb $STELLAR_DEB_URL \
 && dpkg -i stellar-core.deb \
 && rm stellar-core.deb

# ===============================================

FROM debian:jessie-slim

MAINTAINER Viktor Sokolov <gzigzigzeo@evilmartians.com>

ENV STELLAR_CORE_DATABASE_URL "user=gzigzigzeo host=docker.for.mac.localhost dbname=core"
ENV STELLAR_CORE_PEER_PORT 11625
ENV STELLAR_CORE_HTTP_PORT 11626
ENV STELLAR_CORE_BASE_PATH "/var/stellar/core"
ENV STELLAR_CORE_HISTORY_CACHE_SUBPATH "history-cache/vs"

# Dependencies
RUN mkdir -p /usr/share/man/ \
  && mkdir -p /usr/share/man/man1 \
  && mkdir -p /usr/share/man/man2 \
  && mkdir -p /usr/share/man/man3 \
  && mkdir -p /usr/share/man/man4 \
  && mkdir -p /usr/share/man/man5 \
  && mkdir -p /usr/share/man/man6 \
  && mkdir -p /usr/share/man/man7 \
  && mkdir -p /usr/share/man/man8 \
  && mkdir -p /usr/share/man/man9

RUN apt-get update && apt-get -y --no-install-recommends install curl ca-certificates sqlite3 postgresql-client bash && apt-get clean

# Confd
COPY --from=confd /usr/local/bin/confd /usr/local/bin/confd
RUN mkdir -p /etc/confd/templates/
COPY conf.d /etc/confd/conf.d/

# Installation
COPY --from=build /usr/local/bin/stellar-core /usr/local/bin/stellar-core
RUN mkdir -p /var/stellar/core/testnet && mkdir -p /var/stellar/core/pubnet

# Scripts
COPY docker_healthcheck.sh /
RUN chmod +x /docker_healthcheck.sh

COPY docker_entrypoint.sh /
RUN chmod +x /docker_entrypoint.sh

ENTRYPOINT ["/docker_entrypoint.sh"]
CMD ["stellar-core", "--conf", "/etc/stellar-core.cfg"]
EXPOSE ${STELLAR_CORE_HTTP_PORT} ${STELLAR_CORE_PEER_PORT}

HEALTHCHECK CMD ["/docker_healthcheck.sh"]
