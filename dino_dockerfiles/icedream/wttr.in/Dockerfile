# This file contains instructions for Docker on how to build an image that comes
# with the wttr.in files preinstalled and ready to use for ARM hard-float platforms.
#
# Don't forget to add a .wegorc file (by default located in /root/.wegorc) with your
# API key!

FROM alpine:3.4

MAINTAINER Carl Kittelberger <icedream@icedream.pw>

WORKDIR /app

ENV WTTR_GEOLITE /etc/geolite2/GeoLite2-City.mmdb
ENV WTTR_MYDIR /app
ENV WTTR_WEGO /go/bin/wego

CMD python bin/srv.py
EXPOSE 8002

RUN apk --no-cache add \
	ca-certificates \
	py-pip \
	python \
	tzdata \
	&&\
\
	update-ca-certificates

ADD . /app

RUN apk --no-cache add --virtual build-deps \
	gcc \
	git \
	go \
	gzip \
	linux-headers \
	musl-dev \
	python-dev \
	wget \
	&&\
\
	export GOPATH=/go &&\
	mkdir -p "$GOPATH" &&\
	go get -v github.com/schachmat/wego &&\
\
	pip install -r requirements.txt &&\
\
	mkdir -p /etc/geolite2/ &&\
	wget -O- -q http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz |\
	zcat > /etc/geolite2/GeoLite2-City.mmdb &&\
\
	apk del build-deps


