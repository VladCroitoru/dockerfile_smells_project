FROM debian:jessie

MAINTAINER Daniel Holz <dgholz@gmail.com>

RUN apt-get update
RUN apt-get install -y transmission-daemon 
RUN mkdir /transmission
RUN chmod 1777 /transmission

ENV TRANSMISSION_HOME /transmission/config

# Transmission ports
#   HTTP interface
EXPOSE 9091

RUN mkdir /transmission/download
RUN mkdir /transmission/watch
RUN mkdir /transmission/incomplete
RUN mkdir /transmission/config

CMD [ "--allowed", "127.*,10.*,192.168.*,172.16.*,172.17.*,172.18.*,172.19.*,172.20.*,172.21.*,172.22.*,172.23.*,172.24.*,172.25.*,172.26.*,172.27.*,172.28.*,172.29.*,172.30.*,172.31.*,169.254.*", "--watch-dir", "/transmission/watch", "--encryption-preferred", "--foreground", "--config-dir", "/transmission/config", "--incomplete-dir", "/transmission/incomplete", "--dht", "--no-auth", "--download-dir", "/transmission/download" ]
ENTRYPOINT ["/usr/bin/transmission-daemon"]
