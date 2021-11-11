FROM ubuntu:xenial
MAINTAINER ian@phpb.com

ARG BUILD_DATE
ARG VCS_REF
ARG VCS_BRANCH
ARG VERSION

LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.name="Docker PostgreSQL" \
      org.label-schema.description="Dockerized PostgreSQL for use with Gitlab CE" \
      org.label-schema.usage="https://gotfix.com/docker/postgresql/blob/master/README.md" \
      org.label-schema.url="https://gotfix.com/docker/postgresql" \
      org.label-schema.vcs-url=https://gotfix.com/docker/postgresql.git \
      org.label-schema.vendor="Ian Matyssik <ian@phpb.com>" \
      org.label-schema.vcs-ref="${VCS_REF}" \
      org.label-schema.version="${VERSION}" \
      org.label-schema.build-date="${BUILD_DATE}" \
      com.gotfix.maintainer="ian@phpb.com" \
      com.gotfix.license=MIT \
      com.gotfix.docker.dockerfile="/Dockerfile"

ENV PG_APP_HOME="/etc/docker-postgresql"\
    PG_VERSION=9.6 \
    PG_USER=postgres \
    PG_HOME=/var/lib/postgresql \
    PG_RUNDIR=/run/postgresql \
    PG_LOGDIR=/var/log/postgresql \
    PG_CERTDIR=/etc/postgresql/certs

ENV PG_BINDIR=/usr/lib/postgresql/${PG_VERSION}/bin \
    PG_DATADIR=${PG_HOME}/${PG_VERSION}/main

ARG HTTP_PROXY
ARG HTTPS_PROXY
ARG http_proxy
ARG https_proxy

RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \
 && echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \
 && apt-get update \
 && apt-get -yy upgrade \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y vim.tiny curl wget sudo net-tools ca-certificates unzip apt-transport-https \
 && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
 && echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' > /etc/apt/sources.list.d/pgdg.list \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y acl \
    postgresql-${PG_VERSION} postgresql-client-${PG_VERSION} postgresql-contrib-${PG_VERSION} \
 && ln -sf ${PG_DATADIR}/postgresql.conf /etc/postgresql/${PG_VERSION}/main/postgresql.conf \
 && ln -sf ${PG_DATADIR}/pg_hba.conf /etc/postgresql/${PG_VERSION}/main/pg_hba.conf \
 && ln -sf ${PG_DATADIR}/pg_ident.conf /etc/postgresql/${PG_VERSION}/main/pg_ident.conf \
 && rm -rf ${PG_HOME} \
 && rm -rf /var/lib/apt/lists/*

COPY runtime/ ${PG_APP_HOME}/
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

EXPOSE 5432/tcp
VOLUME ["${PG_HOME}", "${PG_RUNDIR}", "${PG_LOGDIR}"]
WORKDIR ${PG_HOME}
ENTRYPOINT ["/sbin/entrypoint.sh"]
