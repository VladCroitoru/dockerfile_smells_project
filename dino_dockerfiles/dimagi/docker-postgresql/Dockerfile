# PostgreSQL service with pghashlib and PL-Proxy

FROM postgres:12

MAINTAINER Dimagi <devops@dimagi.com>

RUN apt-get update && apt-get -y install --no-upgrade \
    gcc \
    make \
    postgresql-$PG_MAJOR-plproxy \
    postgresql-server-dev-$PG_MAJOR \
    python-docutils \
    unzip \
    wget \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://github.com/markokr/pghashlib/archive/master.zip -O pghashlib.zip \
  && unzip pghashlib.zip \
  && cd pghashlib-master \
  && PG_CONFIG=/usr/lib/postgresql/$PG_MAJOR/bin/pg_config make \
  && PG_CONFIG=/usr/lib/postgresql/$PG_MAJOR/bin/pg_config make install \
  && ldconfig

RUN sed -ri "s/^#?(shared_preload_libraries\s*=\s*)\S+/\1'pg_stat_statements'/" /usr/share/postgresql/$PG_MAJOR/postgresql.conf.sample
