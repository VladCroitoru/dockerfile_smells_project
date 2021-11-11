FROM mdillon/postgis:9.6
MAINTAINER Milo van der Linden <milo@dogodigi.net>

ENV PGROUTING_MAJOR 2.3
ENV POSTRES_USER postgres
ENV CARTO_DB_NAME carto_db
ENV CARTO_ENV development

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils\
      git \
      build-essential \
      ca-certificates \
      postgresql-server-dev-$PG_MAJOR \
      postgresql-plpython-$PG_MAJOR \
      postgresql-$PG_MAJOR-pgrouting && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /cartodb-postgresql
RUN git clone --depth 1 --branch master https://github.com/CartoDB/cartodb-postgresql.git /cartodb-postgresql
RUN cd /cartodb-postgresql && make all install

# somehow, we need to run this again. postgresql parent container does this, but it seems to get overwritten
RUN sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!" /usr/share/postgresql/postgresql.conf.sample

RUN mkdir -p /docker-entrypoint-initdb.d
COPY ./initdb-carto.sh /docker-entrypoint-initdb.d/carto.sh
