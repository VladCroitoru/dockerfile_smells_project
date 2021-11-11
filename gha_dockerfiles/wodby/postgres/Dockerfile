ARG POSTGRES_VER

FROM postgres:${POSTGRES_VER}-alpine

ARG POSTGRES_VER
ARG POSTGRES_MAJOR_VER

ARG TARGETPLATFORM

ENV POSTGRES_VER="${POSTGRES_VER}" \
    # Major version: 10.2 => 10, 9.6.3 => 9.6
    # http://www.databasesoup.com/2016/05/changing-postgresql-version-numbering.html
    POSTGRES_MAJOR_VER="${POSTGRES_MAJOR_VER}" \
    POSTGRES_USER="postgres"

RUN set -ex; \
    apk add --no-cache -t .postgres-run-deps \
        ca-certificates \
        make \
        pwgen \
        tar \
        wget; \
    \
    dockerplatform=${TARGETPLATFORM:-linux/amd64};\
    gotpl_url="https://github.com/wodby/gotpl/releases/download/0.3.3/gotpl-${dockerplatform/\//-}.tar.gz"; \
    wget -qO- "${gotpl_url}" | tar xz --no-same-owner -C /usr/local/bin

COPY bin /usr/local/bin
COPY templates /etc/gotpl/
COPY initdb.d /docker-entrypoint-initdb.d/

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["-c", "config_file=/etc/postgresql/postgresql.conf"]
