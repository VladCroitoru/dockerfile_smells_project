FROM postgres:9.6-alpine

ENV PGIS_VERSION 2.3.2

RUN ash -c 'echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories' \
  && apk update \
  && apk add --no-cache --virtual .fetch-deps \
			ca-certificates \
			openssl \
			tar \
  && apk add --no-cache --virtual .build-deps \
	     		bison \
			coreutils \
			flex \
			gcc \
			libc-dev \
			libedit-dev \
			libxml2-dev \
			libxslt-dev \
			make \
			openssl-dev \
			perl \
			util-linux-dev \
			zlib-dev \
  && apk add --no-cache proj4-dev@testing \
     	     		geos-dev@testing \
			gdal-dev@testing \
  && wget http://download.osgeo.org/postgis/source/postgis-$PGIS_VERSION.tar.gz \
  && tar xvzf postgis-$PGIS_VERSION.tar.gz \
  && rm postgis-$PGIS_VERSION.tar.gz \
  && cd postgis-$PGIS_VERSION \
  && make \
  && make install \
  && cd ../ \
  && rm -r postgis-$PGIS_VERSION \
  && apk del .fetch-deps .build-deps \
  && find /usr/local -name '*.a' -delete
