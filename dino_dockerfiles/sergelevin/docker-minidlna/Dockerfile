FROM lsiobase/xenial
MAINTAINER Serge A. Levin <serge.levin.spb@gmail.com>

# global environment settings
ARG DEBIAN_FRONTEND="noninteractive"
ENV HOME="/config"

# install packages
RUN \
 apt-get update && \
 apt-get install -y \
	minidlna && \

# make config template
 cat /etc/minidlna.conf | \
   sed -e 's:^media_dir=.*$:media_dir=/data:' \
       -e 's:^#\?db_dir=.*$:db_dir=/config/cache/minidlna:' \
       -e 's:^#\?log_dir=.*$:log_dir=/config/log:' \
   > /defaults/minidlna.conf && \

# cleanup
 apt-get clean && \
 rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*

# add local files
COPY root/ /

# ports and volumes
EXPOSE 8200 1900/udp
VOLUME /config /data
