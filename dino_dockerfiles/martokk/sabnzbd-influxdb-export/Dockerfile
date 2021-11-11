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
  python /root/sabnzbd_influxdb_export.py \
    --sabnzbdhost=${SABNZBD_HOST} \
    --sabnzbdport=${SABNZBD_PORT} \
    --sabnzbdapikey=${SABNZBD_API_KEY} \
    --influxdbhost=${INFLUXDB_HOST} \
    --influxdbport=${INFLUXDB_PORT}
