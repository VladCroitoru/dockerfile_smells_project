FROM osrm/osrm-backend:v5.8.0
ENV MAP belarus-latest

ADD http://download.geofabrik.de/europe/${MAP}.osm.pbf /data/${MAP}.osm.pbf
#COPY car.lua /opt/car.lua
RUN osrm-extract -p /opt/car.lua /data/${MAP}.osm.pbf
RUN osrm-contract /data/${MAP}.osrm

CMD osrm-routed /data/${MAP}.osrm  --max-matching-size 3000

