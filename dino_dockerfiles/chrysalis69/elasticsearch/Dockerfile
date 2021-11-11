FROM chrysalis69/jre8:latest

MAINTAINER chrysalis69@gmail.com

ENV ELASTICSEARCH_VERSION 2.2.0

RUN ( wget -O /tmp/es.tar.gz https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$ELASTICSEARCH_VERSION/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz && gunzip /tmp/es.tar.gz && cd /opt && tar xf /tmp/es.tar && rm /tmp/es.tar && mv /opt/elasticsearch* /opt/elasticsearch && adduser -D elasticsearch && chown -R elasticsearch:elasticsearch /opt/elasticsearch && mkdir -p /var/log/elasticsearch && chown elasticsearch:elasticsearch /var/log/elasticsearch )

EXPOSE 9200 9300
USER elasticsearch
WORKDIR /opt/elasticsearch

ENTRYPOINT bin/elasticsearch -Des.network.bind_host=_site_ -Des.network.publish_host=_site_ 
