# 2014-11-04
# Peter.Kutschera@ait.ac.at

# docker build -t peterkutschera/osm-cache osm-cache
# docker run -P -d --name=osm-cache peterkutschera/osm-cache
# Load more tiles into the cache:
# docker exec osm-cache ./bin/downloadosmtiles.pl --lat 45:50 --lon 16:18 --zoom 0:7 --destdir=/var/www/OSM

FROM debian:7.7
MAINTAINER Peter.Kutschera@ait.ac.at

RUN apt-get update && apt-get install -y apache2 libgeo-osm-tiles-perl curl unzip && apt-get clean

COPY var/www /var/www/
RUN cd /var/www && \
    curl -O http://code.jquery.com/jquery-2.1.1.min.js && \
    curl -O http://code.jquery.com/jquery-2.1.1.min.map && \
    curl -O http://leaflet-cdn.s3.amazonaws.com/build/leaflet-0.7.3.zip && \
    unzip leaflet-0.7.3.zip -d leaflet-0.7.3 && \
    rm leaflet-0.7.3.zip

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 80

VOLUME /var/www/OSM

WORKDIR /root

COPY root/bin/downloadosmtiles.pl /root/bin/downloadosmtiles.pl
RUN chmod +x /root/bin/*
RUN ./bin/downloadosmtiles.pl --lat -90:90 --lon -180:180 --zoom 0:2 --destdir=/var/www/OSM

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
