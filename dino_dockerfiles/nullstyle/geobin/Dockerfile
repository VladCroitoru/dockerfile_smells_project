FROM postgres:9.4

RUN apt-get update \
    && apt-get install -y postgis \
    && apt-get install -y unzip \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /docker-entrypoint-initdb.d

# add and convert timezone data
COPY data /data
RUN cd /data \
  && unzip tz_world.zip \
  && shp2pgsql -G -s 4326 -I -S -D ./world/tz_world.shp > tz_world.sql

# install db initialization scripts
COPY docker-entrypoint-initdb.d /docker-entrypoint-initdb.d
