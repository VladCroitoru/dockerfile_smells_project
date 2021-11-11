FROM starefossen/pgrouting

LABEL maintainer="pamtrak06@gmail.com" \
      description="osm2pgrouting + osm2pgsql"

RUN apt-get update -y && \
    apt-get install -y git pkg-config build-essential

# osm2pgrouting Requirements
RUN apt-get install -y  cmake expat libexpat1-dev \
  libboost-dev libboost-program-options-dev libpqxx-dev

# compile osm2pgrouting
ENV OSM_2_PGROUTING_VERSION=2.3.3
RUN git clone https://github.com/pgRouting/osm2pgrouting.git
RUN cd osm2pgrouting && \
    git fetch --all && git checkout v${OSM_2_PGROUTING_VERSION} && \
    cmake -H. -Bbuild && \
    cd build/ && make && make install

# osm2pgsql Requirements$
RUN apt-get install -y make cmake g++ libboost-dev libboost-system-dev \
   libboost-filesystem-dev libexpat1-dev zlib1g-dev \
   libbz2-dev libpq-dev libproj-dev lua5.2 liblua5.2-dev

# compile osm2pgsql
ENV OSM_2_PGRSQL_VERSION=0.94.0
RUN git clone git://github.com/openstreetmap/osm2pgsql.git && \
    cd osm2pgsql && \
    git fetch --all && git checkout ${OSM_2_PGRSQL_VERSION} && \
    mkdir build && cd build && cmake .. && \
    make && make install

# Setup home environment
ENV PKG_CONFIG_PATH /root/lib/pkgconfig
ENV LD_LIBRARY_PATH /root/lib

ADD bashrc /root/.bashrc


