FROM docker.elastic.co/elasticsearch/elasticsearch:5.6.1

MAINTAINER JamesMo <springclick@gmail.com>

ADD config/elasticsearch.yml /usr/share/elasticsearch/config/
USER root
RUN chown elasticsearch:elasticsearch config/elasticsearch.yml
USER elasticsearch
