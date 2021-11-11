FROM docker.elastic.co/elasticsearch/elasticsearch:6.6.0

LABEL maintainer="lucacri@gmail.com"

COPY files/ /

RUN mv /elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml && \
    chmod 777 /start.sh && \
    chmod 777 /usr/share/elasticsearch/config/elasticsearch.yml

USER root

ENV ES_JAVA_OPTS="-Xms2g -Xmx2g" \
    node.master="true" \
    node.data="true" \
    node.ingest="true" \
    bootstrap.memory_lock="false" \
    cluster.name="es-cluster" \
    network.host="0.0.0.0" \
    PROCESSORS="1" \
    xpack.security.enabled="false" 

ENTRYPOINT [ "/start.sh" ]