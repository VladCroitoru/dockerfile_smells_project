FROM alpine:3.3

MAINTAINER Edouard Fischer <edouard.fischer@gmail.com>

RUN mkdir -p /usr/src/geoip
WORKDIR /usr/src/geoip

RUN wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz && gunzip *.gz

VOLUME /usr/src/geoip

CMD [ "sh"]
