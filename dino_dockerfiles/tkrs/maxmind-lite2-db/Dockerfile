FROM gliderlabs/alpine:3.2

MAINTAINER Takeru Sato <midium.size@gmail.com>

ENV GEOIP_DB_DL_URL_PREF    http://geolite.maxmind.com/download/geoip/database
ENV GEOIP_CNTR_DB           GeoLite2-Country.mmdb
ENV GEOIP_CITY_DB           GeoLite2-City.mmdb
ENV GEOIP_DB_DIR            /usr/share/GeoIP

ADD ${GEOIP_DB_DL_URL_PREF}/${GEOIP_CNTR_DB}.gz /tmp/
ADD ${GEOIP_DB_DL_URL_PREF}/${GEOIP_CITY_DB}.gz /tmp/

RUN mkdir -p ${GEOIP_DB_DIR} \
 && gunzip -c /tmp/${GEOIP_CNTR_DB}.gz > ${GEOIP_DB_DIR}/${GEOIP_CNTR_DB} \
 && gunzip -c /tmp/${GEOIP_CITY_DB}.gz > ${GEOIP_DB_DIR}/${GEOIP_CITY_DB} \
 && rm -f /tmp/GeoLite2-*

VOLUME ${GEOIP_DB_DIR}
