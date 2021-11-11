FROM debian:8.4
MAINTAINER Philip Beelmann <beelmann@geofabrik.de>

RUN apt-get update && apt-get install -y \
    gdal-bin \
    node-carto \
    libwww-perl \
    apache2 \
    libmapnik2.2 \
    mapnik-utils \
    libjson-perl \
    libipc-sharelite-perl \
    libgd-gd2-perl \
    unzip \
    git \
    wget \
    curl \
    ttf-dejavu \
    fonts-droid \
    ttf-unifont \
    fonts-sipa-arundina \
    fonts-sil-padauk \
    fonts-khmeros \
    fonts-taml-tscu \
    python-yaml

COPY slippymap.html /var/www/html/osm/
COPY style.css /var/www/html/osm/
COPY restart.sh /usr/local/bin/
COPY debs /tmp/debs
COPY tirex.conf.patch /tmp/
COPY mapnik.conf.patch /tmp/
RUN dpkg -i /tmp/debs/*deb 

COPY tileserver_site.conf /etc/apache2/sites-available/

RUN \
# tirex config
    patch -l /etc/tirex/tirex.conf < /tmp/tirex.conf.patch \
 && patch -l /etc/tirex/renderer/mapnik.conf < /tmp/mapnik.conf.patch \
## install map styles
# osm-bright
 && mkdir -p /srv; cd /srv \
 && git clone https://github.com/mapbox/osm-bright.git \
 && cd osm-bright/ \
 && git remote add rory https://github.com/rory/osm-bright.git \
 && git fetch rory \
 && git checkout rory/master \
# osm-bright - get-shapefiles
 && mkdir shp; cd shp \
 && wget http://data.openstreetmapdata.com/simplified-land-polygons-complete-3857.zip \
 && unzip simplified-land-polygons-complete-3857.zip \
 && wget http://data.openstreetmapdata.com/land-polygons-split-3857.zip \
 && unzip land-polygons-split-3857.zip \
 && wget http://mapbox-geodata.s3.amazonaws.com/natural-earth-1.4.0/cultural/10m-populated-places-simple.zip \
 && mkdir 10m-populated-places-simple; cd 10m-populated-places-simple; unzip ../10m-populated-places-simple.zip \
# openstreetmap-carto
 && mkdir -p /srv; cd /srv \
 && git clone https://github.com/gravitystorm/openstreetmap-carto \
 && cd openstreetmap-carto \
 && ./get-shapefiles.sh \
# create tile directories
 && install -d -o tirex -g tirex /var/lib/tirex/tiles/osmbright/ \
 && install -d -o tirex -g tirex /var/lib/tirex/tiles/osmcarto/ \
 && rm -rf /var/lib/mod_tile \
 && ln -s /var/lib/tirex/tiles /var/lib/mod_tile \
 && chown tirex:tirex -R /var/lib/tirex/tiles/ 

EXPOSE 80

VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"]

COPY osmbright_configure.py /srv/osm-bright/configure.py
COPY osmbright.conf /etc/tirex/renderer/mapnik/
COPY osmcarto_project.yaml /srv/openstreetmap-carto/project.yaml
COPY osmcarto.conf /etc/tirex/renderer/mapnik/

RUN cd /srv/osm-bright \
 && ./make.py \
 && cd OSMBright \
 && carto project.mml > project.xml \
 && cd /srv/openstreetmap-carto/scripts/; python yaml2mml.py \
 && carto /srv/openstreetmap-carto/project.mml > /srv/openstreetmap-carto/project.xml

RUN apt-get update && apt-get install -y postgresql
COPY ./wait-for-postgres.sh /
COPY ./start.sh /usr/local/bin

CMD /usr/local/start.sh

