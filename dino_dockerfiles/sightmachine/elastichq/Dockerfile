FROM nginx:1.13.0

MAINTAINER ops@sightmachine.com

# ENV VERSION 2.0.3

RUN \
  apt-get update && \
  apt-get install -y zip unzip && \
  apt-get autoremove -y -q && \
  apt-get clean -y -q

# ADD https://github.com/royrusso/elasticsearch-HQ/archive/v${VERSION}.zip /tmp/elasticsearch-HQ-${VERSION}.zip
ADD https://github.com/royrusso/elasticsearch-HQ/zipball/master /tmp/master.zip

RUN \
  unzip -q /tmp/master.zip -d /tmp && \
  mv -f /tmp/royrusso-elasticsearch-HQ-* /tmp/elasticsearch-HQ && \
  mv -f /tmp/elasticsearch-HQ/* /usr/share/nginx/html && \
  rm -rf /tmp/*

RUN \
  sed -ie 's/id="connectionURL"/& value="http:\/\/elasticsearch.k8s-uw2.sightmachine.com:9200"/g' /usr/share/nginx/html/index.html
