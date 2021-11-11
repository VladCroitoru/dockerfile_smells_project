FROM ubuntu:latest

MAINTAINER Veedubin <veedubin@comcast.net>

VOLUME ["/data/transmission/downloads"]
VOLUME ["/data/transmission/torrents"]
VOLUME ["/data/transmission/settings"]

# Install transmission-daemon package
RUN export DEBIAN_FRONTEND='noninteractive' && \
apt-get update -qq && \
apt-get install -qqy --no-install-recommends transmission-daemon && \
apt-get -s dist-upgrade && \
apt-get clean

RUN chown -R 1000:1000 /var/lib/transmission-daemon/

USER debian-transmission

EXPOSE 9091 51413/tcp 51413/udp

ADD settings.json /var/lib/transmission-daemon/settings/settings.json

ENTRYPOINT ["transmission-daemon", "--foreground", "--config-dir", "/data/transmission", "--log-error"]
