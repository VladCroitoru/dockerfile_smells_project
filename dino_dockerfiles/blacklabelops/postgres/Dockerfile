FROM blacklabelops/alpine:3.4
MAINTAINER Steffen Bleul <sbl@blacklabelops.com>

# Build time arguments
# Values: latest or version number (e.g. 9.4.6-r0)
ARG POSTGRES_VERSION=latest

RUN apk add --update \
      curl \
      gpgme && \
    if  [ "${POSTGRES_VERSION}" = "latest" ]; \
      then apk add postgresql ; \
      else apk add "postgresql=${POSTGRES_VERSION}" ; \
    fi && \
    # Install gosu
    curl -fsSL https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 -o /usr/local/bin/gosu && \
    chmod +x /usr/local/bin/gosu && \
    # Remove obsolete packages
    apk del \
      curl \
      gpgme && \
    # Clean caches and tmps
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf /var/log/*

ENV LANG en_US.utf8
ENV PGDATA /var/lib/postgresql/data

COPY docker-entrypoint.sh /

VOLUME ["/var/lib/postgresql"]
EXPOSE 5432
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["postgres"]
