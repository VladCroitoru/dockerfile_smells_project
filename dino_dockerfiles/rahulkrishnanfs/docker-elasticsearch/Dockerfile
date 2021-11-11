FROM ubuntu:latest
LABEL Maintainer " Rahulkrisnan R A"
ENV VERSION 5.4.0

RUN apt-get update && apt-get install apt-transport-https  wget -y \
    && echo "deb https://artifacts.elastic.co/packages/${VERSION}/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-${VERSION}.list \
    && wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch |  apt-key add - \
    && apt-get install elasticsearch -y  

ENV PATH $PATH:/usr/share/elasticsearch/bin
WORKDIR /usr/share/elasticsearch
RUN for path in ./plugins ./data ./config ./logs ./bin ; do \
      mkdir -p "$path" ; \
      chown -R elasticsearch:elasticsearch "$path"; \
    done
COPY ./config config
ENV NODE_NAME RAhul
ENV CLUSTER_NAME elastic
ENV NODE_MASTER true
ENV NODE_DATA false
ENV NODE_MAX_LOCAL_STORAGE_NODES 1
ENV INDEX_NO_OF_SHARDS 5
ENV INDEX_NO_OF_REPLICAS 1
ENV NETWORK_HOST _non_loopback:ipv4_
ENV DISCOVERY elastic-discovery
EXPOSE 9300 9200

ENTRYPOINT ["elasticsearch"]
