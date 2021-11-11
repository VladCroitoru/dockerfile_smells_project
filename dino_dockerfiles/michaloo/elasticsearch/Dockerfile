FROM debian:jessie
MAINTAINER Michal Raczka me@michaloo.net

# Expose port 9200
EXPOSE 9200

ENV PATH_CONF /opt/elasticsearch/config
ENV PATH_DATA /opt/elasticsearch/data

VOLUME [ "/opt/elasticsearch/data" ]

WORKDIR /app

# Start Elasticsearch
CMD ["/app/bin/start"]

# Install Java
RUN apt-get update \
    && apt-get install -y openjdk-7-jre-headless curl

# Install Elasticsearch
RUN mkdir -p /opt/elasticsearch \
    && curl https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.2.tar.gz \
    | tar -xz -C /opt/elasticsearch --strip-components=1

# Install plugins
RUN /opt/elasticsearch/bin/plugin -install lmenezes/elasticsearch-kopf \
    && /opt/elasticsearch/bin/plugin -url http://download.elasticsearch.org/kibana/kibana/kibana-latest.zip -install elasticsearch/kibana3 \
    && /opt/elasticsearch/bin/plugin -install royrusso/elasticsearch-HQ

COPY ./bin    /app/bin
COPY ./config /app/config
