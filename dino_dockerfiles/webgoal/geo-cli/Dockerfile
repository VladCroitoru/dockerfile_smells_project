FROM ubuntu:16.04

RUN apt-get update -qq \
  && apt-get install -y --no-install-recommends build-essential curl \
  postgresql-client postgis wget vim python pkg-config bash-completion \
  && rm -rf /var/lib/apt/lists/*

ENV LD_LIBRARY_PATH /usr/local/lib/

WORKDIR /usr/src/app

RUN wget http://download.osgeo.org/gdal/2.2.1/gdal-2.2.1.tar.gz
RUN tar xzvf gdal-2.2.1.tar.gz
RUN rm -f gdal-2.2.1.tar.gz

WORKDIR /usr/src/app/gdal-2.2.1

RUN ./configure
RUN make install

WORKDIR /usr/src/app
RUN rm -rf /usr/src/app/gdal-2.2.1

RUN ogr2ogr --version
RUN shp2pgsql | grep RELEASE
