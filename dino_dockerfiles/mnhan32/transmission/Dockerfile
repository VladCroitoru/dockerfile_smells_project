FROM docker.io/alpine:latest

Run \
apk add --update transmission-daemon && \
mkdir -p /transmission/download && \
mkdir -p /transmission/watch && \
mkdir -p /transmission/incomplete && \
mkdir -p /transmission/config && \
chmod 1777 /transmission

ENV TRANSMISSION_HOME /transmission/config

#expose port
EXPOSE 9091

#run service
ENTRYPOINT ["/usr/bin/transmission-daemon"]

#allow only local access
CMD [ "--allowed", "127.0.0.1,192.168.1.*,172.17.0.*", "--watch-dir", "/transmission/watch", "--encryption-preferred", "--foreground", "--config-dir", "/transmission/config", "--incomplete-dir", "/transmission/incomplete", "--dht", "--no-auth", "--download-dir", "/transmission/download"]
