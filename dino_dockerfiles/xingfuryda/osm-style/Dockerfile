## -*- docker-image-name: "xingfuryda/osm-style:latest" -*-

##
# MapBox Studio Classic
#
# This creates an image with MapBox Studio Classic
#

FROM phusion/baseimage:0.9.18
MAINTAINER xingfuryda

# install packages
RUN apt-get update -y
RUN apt-get install -y postgresql-client nodejs-legacy npm git unzip \
 python-pip python-dev build-essential \
 fonts-dejavu-core fonts-droid ttf-unifont fonts-sipa-arundina fonts-sil-padauk \
 fonts-khmeros fonts-beng-extra fonts-gargi fonts-taml-tscu fonts-tibetan-machine \
 fonts-dejavu-extra ttf-indic-fonts-core ttf-kannada-fonts 
 
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv
RUN pip install pyyaml

# build mapbox-studio-classic
RUN mkdir /home/root
RUN cd /home/root && git clone git://github.com/mapbox/mapbox-studio-classic.git && \
 cd mapbox-studio-classic && git checkout 6b67bb95d234631e6076780bccbdfac6471035cf
# fix to allow large POST
RUN sed -i "s/app.use(bodyParser.json());/app.use(bodyParser.json({limit:1024*1024*50, type:'application\/json'}));/" \
 /home/root/mapbox-studio-classic/lib/server.js
RUN cd /home/root/mapbox-studio-classic && npm install

# Install mapbox sql scripts
RUN cd /home/root && git clone git://github.com/mapbox/postgis-vt-util.git  
RUN cd /home/root/postgis-vt-util && git checkout cd52a4d5eb5d9768ccb2fa907d06a863e983f8a7

# Install openstreetmap-carto-vector
RUN cd /home/root && git clone git://github.com/geofabrik/openstreetmap-carto-vector-tiles.git && \
 cd openstreetmap-carto-vector-tiles && git checkout vector-tiles && \
 git checkout fb863ad519141bdda6c52967bc73c53b2f53ad73

# configure openstreetmap-carto-vector
RUN cd /home/root/openstreetmap-carto-vector-tiles && npm install mapnik && ls && ./get-shapefiles.sh

RUN apt-get install -y sqlite3

# install tessera
RUN mkdir /home/root/tessera
RUN cd /home/root/tessera && npm install tessera
RUN cd /home/root/tessera && npm install mbtiles
RUN cd /home/root/tessera && npm install tilelive-carto
RUN cd /home/root/tessera && npm install tilelive-tmstyle
RUN cd /home/root/tessera && npm install tilelive-tmsource
RUN cd /home/root/tessera && npm install tilelive-http
RUN cd /home/root/tessera && npm install tilelive-mapnik
RUN cd /home/root/tessera && npm install tilelive-xray

# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add the entrypoint
ADD run.sh /usr/local/sbin/run
RUN chmod +x /usr/local/sbin/run
ENTRYPOINT ["/sbin/my_init", "--", "/usr/local/sbin/run"]

ADD updateConnection.py /home/root/openstreetmap-carto-vector-tiles
ADD narrowStyleTabs.py /home/root/openstreetmap-carto-vector-tiles
RUN python /home/root/openstreetmap-carto-vector-tiles/narrowStyleTabs.py
ADD patchtilelive.py /home/root/openstreetmap-carto-vector-tiles
RUN python /home/root/openstreetmap-carto-vector-tiles/patchtilelive.py
ADD patchTemplates.py /home/root/openstreetmap-carto-vector-tiles
RUN python /home/root/openstreetmap-carto-vector-tiles/patchTemplates.py