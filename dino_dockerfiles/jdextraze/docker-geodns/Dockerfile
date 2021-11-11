FROM golang:1.6.0

# Install the GeoIP C library.
RUN apt-get update \
 && apt-get install -y libgeoip-dev pkg-config

# Download the GeoIP data files from Maxmind.
# No GeoLite2 support yet, see https://github.com/abh/geodns/issues/66
RUN cd /usr/share/GeoIP \
 && rm -f * \
 && wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz \
 && wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz \
 && wget http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz \
 && gzip -d GeoIP.dat.gz \
 && gzip -d GeoLiteCity.dat.gz \
 && gzip -d GeoIPASNum.dat.gz \
 && mv GeoLiteCity.dat GeoIPCity.dat

# Download, test & build the GeoDNS server.
RUN go get github.com/abh/geodns \
 && cd $GOPATH/src/github.com/abh/geodns \
 && go get -t \
 && go test \
 && go build

 EXPOSE 53
 EXPOSE 8053

RUN mkdir /dns
WORKDIR $GOPATH/src/github.com/abh/geodns
CMD ./geodns -config="/dns"
VOLUME /dns
