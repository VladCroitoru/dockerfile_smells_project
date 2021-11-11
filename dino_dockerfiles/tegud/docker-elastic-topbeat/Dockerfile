FROM ubuntu:trusty
MAINTAINER Steve Elliott <steve@tegud.net>

RUN apt-get update && apt-get install -y curl

ENV TOPBEAT_VERSION=1.2.3

RUN curl -L -O https://download.elastic.co/beats/topbeat/topbeat_${TOPBEAT_VERSION}_amd64.deb && \
    sudo dpkg -i topbeat_${TOPBEAT_VERSION}_amd64.deb && \
    mv /etc/topbeat/topbeat.yml /etc/topbeat/topbeat.example.yml

run curl -L -O http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz && \
    mkdir -p /usr/share/GeoIP && \
    gunzip -c GeoLiteCity.dat.gz > /usr/share/GeoIP/GeoLiteCity.dat

WORKDIR /topbeat

ADD files/ .

CMD /topbeat/start.sh
