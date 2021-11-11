FROM openshift/base-centos7

ENV \
      PG_VERSION=94 \
      PG_MAJOR=9.4 \
      PGDATA=/var/lib/pgsql/data

USER root

RUN \
  set -ex; \
  yum install -y http://packages.2ndquadrant.com/postgresql-bdr${PG_VERSION}-2ndquadrant/yum-repo-rpms/postgresql-bdr${PG_VERSION}-2ndquadrant-redhat-latest.noarch.rpm ; \
  yum update -y yum-skip-broken ; \
  yum install -y postgresql-bdr${PG_VERSION}-bdr ; \
  \
  yum clean all ; \
  rm -rf /var/cache/yum

RUN \
  set -ex; \
  mkdir -p /var/run/postgresql ; \
  mkdir -p $PGDATA ; \
  \
  fix-permissions /var/run/postgresql ; \
  fix-permissions $PGDATA ; \
  chown -R postgres:postgres $PGDATA 

ADD postgresql-entrypoint.sh /
ADD replicate.sh /docker-entrypoint-initdb.d/

RUN chmod +x /postgresql-entrypoint.sh && \
    chmod +x /docker-entrypoint-initdb.d/replicate.sh

ENV PATH /usr/pgsql-${PG_MAJOR}/bin:$PATH

EXPOSE 5432

USER postgres

ENTRYPOINT [ "/postgresql-entrypoint.sh" ]

CMD ["postgres"]
