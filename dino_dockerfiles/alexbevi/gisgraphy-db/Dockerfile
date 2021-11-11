FROM mdillon/postgis:latest
MAINTAINER Ruggero Marchei <ruggero.marchei@daemonzone.net>

ENV GISGRAPHY_VERSION 4.0-beta1
ENV GISGRAPHY_MD5 2bc368aee43c6b02b4e415cbf15edb88

RUN cd /tmp \
  && apt-get update \
  && apt-get install -y --no-install-recommends bsdtar curl \
  && curl -s -O http://download.gisgraphy.com/releases/gisgraphy-$GISGRAPHY_VERSION.zip \
  && echo "$GISGRAPHY_MD5  gisgraphy-$GISGRAPHY_VERSION.zip" > gisgraphy-$GISGRAPHY_VERSION.zip.md5 \
  && md5sum -c gisgraphy-$GISGRAPHY_VERSION.zip.md5 \
  && bsdtar -C /docker-entrypoint-initdb.d/ -x -f /tmp/gisgraphy-$GISGRAPHY_VERSION.zip --strip-components=2 *sql/create_tables.sql */sql/insert_users.sql \
  && rm -f /tmp/gisgraphy* \
  && apt-get purge -y bsdtar curl \
  && apt-get autoremove --purge -y \
  && rm -rf /var/lib/apt/lists/*

RUN cd /docker-entrypoint-initdb.d \
  && mv postgis.sh 10-postgis.sh \
  && mv create_tables.sql 20-create_tables.sql \
  && mv insert_users.sql 30-insert_users.sql

ENV POSTGRES_DB gisgraphy
