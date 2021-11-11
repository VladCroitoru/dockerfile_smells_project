##
# The OpenStreetMap Tile Server
#
# This creates an image with containing the OpenStreetMap tile server stack as
# described at
# <http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/>.
#

FROM phusion/baseimage:0.9.16

MAINTAINER Christian Linder <rednil@onyown.de>

# Set the locale. This affects the encoding of the Postgresql template
# databases.
ENV LANG C.UTF-8
RUN update-locale LANG=C.UTF-8

RUN add-apt-repository -y ppa:kakrueger/openstreetmap

# Install dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y && apt-get upgrade -y && apt-get install -y \
libapache2-mod-tile \
bzip2 \
fonts-taml-tscu \
fonts-tibetan-machine \
git-core \
libicu-dev \
mapnik-utils \
npm \
postgresql-server-dev-all \
python-gdal \
python-mapnik \
python-software-properties \
python-yaml \
software-properties-common \
subversion \
tar \
ttf-dejavu && \
cd /etc/mapnik-osm-carto-data/data && rm *.zip *.tgz 

# Install node and some npm modules
RUN ln -s /usr/bin/nodejs /usr/bin/node && npm install -g carto shelljs minimist point-in-polygon request unzip

ENV OPENSTREETMAP_CARTO_VERSION=v2.29.1

# Install the Mapnik stylesheet
RUN cd /usr/local/src && git clone -b $OPENSTREETMAP_CARTO_VERSION --depth=1 https://github.com/gravitystorm/openstreetmap-carto.git mapnik-style

# Fetch postgres functions required for localized labels on the map
RUN cd /usr/local/src && svn co http://svn.openstreetmap.org/applications/rendering/mapnik-german/utf8translit
RUN cd /usr/local/src && wget http://svn.openstreetmap.org/applications/rendering/mapnik-german/views/get_localized_name.sql
# build the utf8translit function required for localization
RUN cd /usr/local/src/utf8translit && make && make install

# Expose the webserver and database ports
EXPOSE 80 5432

# We need the volume for importing data from
VOLUME ["/var/www"]

# Set the osm2pgsql import cache size in MB. Used in `run import`.
ENV OSM_IMPORT_CACHE 800

CMD ["/sbin/my_init"]

# The preferred language for labels on the map, defaults to german ("de")
ENV PREFERRED_LANGUAGE en

# Copy all required files into the docker container
COPY filesystem /

# do all init work that doesn't require huge downloads 
RUN /usr/local/sbin/build.sh

