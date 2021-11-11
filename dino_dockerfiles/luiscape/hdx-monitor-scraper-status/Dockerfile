###########################################################
# Image that runs a status collection service for scrapers.
# Receives link from a MongoDB container and links to the
# hdx-monitor-server.
###########################################################

FROM node:latest

MAINTAINER Luis Capelo <capelo@un.org>

RUN \
  apt-get install git \
  && git clone http://github.com/luiscape/hdx-monitor-scraper-status \
  && cd hdx-monitor-scraper-status \
  && make configure

WORKDIR '/hdx-monitor-scraper-status'

EXPOSE 9000

CMD ['make', 'run']
