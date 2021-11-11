FROM library/debian:wheezy
MAINTAINER Josep <jribes7@xtec.cat>
# Minimal changes to httpd
RUN apt-get update && \
apt-get -y upgrade && \
apt-get install -y mplayer && \
apt-get clean && apt-get autoclean && \
rm -rf /var/lib/apt/lists/*
