ARG FROM_IMG=qnib/alplain-jre8
ARG DOCKER_REGISTRY=docker.io
FROM ${DOCKER_REGISTRY}/${FROM_IMG}

VOLUME ["/opt/neo4j/data", "/opt/neo4j/logs", "/opt/neo4j/run"]

ARG NEO_VER=3.3.0
ENV ENTRYPOINTS_DIR=/opt/qnib/entry/ \
    NEO_DBMS_LISTEN_ADDR=0.0.0.0 \
    NEO_BOLT_ADDRESS=0.0.0.0 \
    NEO_BOLT_PORT=7687 \
    NEO_HTTP_ADDRESS=0.0.0.0 \
    NEO_HTTP_PORT=7474 \
    NEO_HTTPS_ADDRESS=0.0.0.0 \
    NEO_HTTPS_PORT=7473 \
    NEO_AUTH_ENABLED=false \
    NEO_HEAP_INIT=512m \
    NEO_HEAP_MAX=512m
RUN mkdir -p /opt/neo4j \
 && wget -qO - https://neo4j.com/artifact.php?name=neo4j-community-${NEO_VER}-unix.tar.gz |tar xfz - --strip-components=1 -C /opt/neo4j
COPY opt/qnib/neo4j/bin/start.sh /opt/qnib/neo4j/bin/
COPY opt/qnib/neo4j/conf/neo4j.conf /opt/qnib/neo4j/conf/
COPY opt/qnib/entry/30-config-neo4j.sh /opt/qnib/entry/
CMD ["/opt/qnib/neo4j/bin/start.sh"]
