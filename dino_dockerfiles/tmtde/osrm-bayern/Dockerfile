FROM osrm/osrm-backend
MAINTAINER Timo Lindenblatt <timo.lindenblatt@tmt.de>
RUN wget http://download.geofabrik.de/europe/germany/bayern-latest.osm.pbf -P /data && \
osrm-extract -p /opt/car.lua /data/bayern-latest.osm.pbf && \
osrm-contract /data/bayern-latest.osrm
WORKDIR /data
CMD osrm-routed /data/bayern-latest.osrm
