FROM	alpine:latest

# Install Packages
RUN	\
  apk update && \
  apk upgrade && \
	apk add python py-requests py-pip && \
	pip install influxdb

# cleanup
RUN \
 apk del --purge && \
 rm -rf \
	/root/.cache

# add local files
COPY . /root/

# Run script
CMD \
  python /root/qbittorrent_influxdb_export.py \
    --qbittorrenthost=${QBITTORRENT_HOST} \
    --qbittorrentport=${QBITTORRENT_PORT} \
    --qbittorrentuser=${QBITTORRENT_USER} \
    --qbittorrentpassword=${QBITTORRENT_PASSWORD} \
    --influxdbhost=${INFLUXDB_HOST} \
    --influxdbport=${INFLUXDB_PORT}
