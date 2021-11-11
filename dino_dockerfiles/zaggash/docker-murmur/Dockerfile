FROM lsiobase/alpine

LABEL maintainer "zaggash"

ENV MURMUR_VERSION=1.2.19

# install packages
RUN \
 apk add --no-cache --virtual=build-dependencies \
 	curl && \
 apk add --no-cache \
 	openssl \
	icu-libs && \
	
 wget -q \
        https://github.com/mumble-voip/mumble/releases/download/${MURMUR_VERSION}/murmur-static_x86-${MURMUR_VERSION}.tar.bz2 -O - |\
        bzcat -f |\
        tar -x -C /app -f - && \
  mv /app/murmur* /app/murmur && \
  
  apk del --purge \
	build-dependencies && \
  rm -rf /var/cache/apk/* /tmp/*

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 64738
VOLUME /config
