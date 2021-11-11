## -*- docker-image-name: "xingfuryda/openstreetmap-tiles-docker:latest" -*-

##
# The OpenStreetMap Import Server
#
# This creates an image with osm2pgsql as described at
# <http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/>.
#
# forked and adapted from geo-data/openstreetmap-tiles-docker

FROM phusion/baseimage:0.9.17
MAINTAINER xingfuryda

# Set the locale. This affects the encoding of the Postgresql template
# databases.
ENV LANG C.UTF-8
RUN update-locale LANG=C.UTF-8

# Ensure `add-apt-repository` is present
RUN apt-get update -y
RUN apt-get install -y software-properties-common python-software-properties

# Install postgresql and postgis
RUN apt-get install -y wget
RUN locale-gen en_US.UTF-8
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' | sudo tee /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql-9.4-postgis postgresql-contrib postgresql-server-dev-9.4

# install compiler
RUN apt-get install -y gcc-4.8 g++-4.8
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 20
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 20
RUN update-alternatives --config gcc
RUN update-alternatives --config g++

RUN apt-get install -y build-essential make cmake libboost1.55-dev libboost-filesystem1.55-dev libboost-program-options1.55-dev libboost-python1.55-dev libboost-regex1.55-dev libboost-system1.55-dev libboost-thread1.55-dev

# Install osm2pgsql dependencies
RUN apt-get install -y subversion git git-core tar unzip libbz2-dev bzip2 libtool libxml2-dev libgeos-dev libpq-dev munin-node munin libprotobuf-c0-dev protobuf-c-compiler libprotobuf-dev protobuf-compiler pkg-config libfreetype6-dev libpng12-dev libtiff4-dev libicu-dev libgdal-dev libcairo-dev libcairomm-1.0-dev libagg-dev liblua5.2-dev ttf-unifont libgeos++-dev libproj-dev gdal-bin libgdal1-dev

# Install osm2pgsql
RUN cd /tmp && git clone git://github.com/openstreetmap/osm2pgsql.git
RUN cd /tmp/osm2pgsql && mkdir build && cd build && cmake ..
RUN cd /tmp/osm2pgsql/build && make && make install

# Ensure the www-data user can connect to the gis database
RUN sed -i -e 's/local   all             all                                     peer/local gis www-data peer/' /etc/postgresql/9.4/main/pg_hba.conf
RUN echo "host    all         all         0.0.0.0/0         trust" >> /etc/postgresql/9.4/main/pg_hba.conf

# Tune postgresql
ADD postgresql.conf.sed /tmp/
RUN sed --file /tmp/postgresql.conf.sed --in-place /etc/postgresql/9.4/main/postgresql.conf

# Define the application logging logic
ADD syslog-ng.conf /etc/syslog-ng/conf.d/local.conf
RUN rm -rf /var/log/postgresql

# Create a `postgresql` `runit` service
ADD postgresql /etc/sv/postgresql
RUN chmod +x /etc/sv/postgresql/run
RUN chmod +x /etc/sv/postgresql/check
RUN chmod +x /etc/sv/postgresql/down
RUN update-service --add /etc/sv/postgresql

# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose the webserver and database ports
EXPOSE 5432

# We need the volume for importing data from
VOLUME ["/data"]

# Set the osm2pgsql import cache size in MB. Used in `run import`.
ENV OSM_IMPORT_CACHE 800

# Add the README
ADD README.md /usr/local/share/doc/

# Add the help file
RUN mkdir -p /usr/local/share/doc/run
ADD help.txt /usr/local/share/doc/run/help.txt

# Add the entrypoint
ADD run.sh /usr/local/sbin/run
RUN chmod +x /usr/local/sbin/run
ENTRYPOINT ["/sbin/my_init", "--", "/usr/local/sbin/run"]

# Default to showing the usage text
CMD ["help"]
