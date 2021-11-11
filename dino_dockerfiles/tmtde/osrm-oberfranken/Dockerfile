FROM osrm/osrm-backend
MAINTAINER Timo Lindenblatt <timo.lindenblatt@tmt.de>
RUN wget http://download.geofabrik.de/europe/germany/bayern/oberfranken-latest.osm.pbf -P /data && \
osrm-extract -p /opt/car.lua /data/oberfranken-latest.osm.pbf && \
osrm-contract /data/oberfranken-latest.osrm
WORKDIR /data
CMD osrm-routed /data/oberfranken-latest.osrm
