FROM mdillon/postgis:9.4

MAINTAINER Jakob Langdal "jakob@langdal.dk"

RUN apt-get update \
  && apt-get -y install postgresql-9.4-pgrouting \
  && rm -rf /var/lib/apt/lists/*
