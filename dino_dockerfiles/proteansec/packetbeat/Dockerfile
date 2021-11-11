FROM phusion/baseimage:0.9.16
MAINTAINER Dejan Lukan <dejan@proteansec.com>

RUN apt-get update --fix-missing
RUN apt-get -y -q install libpcap0.8 curl unzip

# Install PacketBeat
ENV VERSION 1.0.0-beta4
ADD https://download.elastic.co/beats/packetbeat/packetbeat_${VERSION}_amd64.deb .
RUN dpkg -i packetbeat_${VERSION}_amd64.deb

# Configuration file
RUN mkdir -p /etc/packetbeat/
ADD packetbeat.yml /etc/packetbeat/packetbeat.yml

# GeoIP
RUN mkdir -p /usr/local/share/GeoIP/
ADD http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz /usr/local/share/GeoIP/GeoIP.dat.gz
RUN gunzip /usr/local/share/GeoIP/GeoIP.dat.gz

# entry point takes care of setting conf values
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh
ENTRYPOINT ["/sbin/entrypoint.sh"]

CMD ["app:start"]
