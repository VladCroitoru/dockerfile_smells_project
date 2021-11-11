# Neo4j Server
# Repository http://github.com/jedivind/docker-neo4j
FROM java:openjdk-8-jre

MAINTAINER Vinay Bharadwaj <vbharadwaj@milcord.com>

ENV PATH $PATH:/var/lib/neo4j/bin

ENV NEO4J_VERSION 2.1.5

RUN apt-get update \
    && apt-get install -y curl \
    && curl -fSL -o neo4j-community.tar.gz http://dist.neo4j.org/neo4j-community-$NEO4J_VERSION-unix.tar.gz \
    && tar xzf neo4j-community.tar.gz -C /var/lib \
    && mv /var/lib/neo4j-* /var/lib/neo4j \
    && ln -s /var/lib/neo4j/data /data \
    && touch /tmp/rrd \
    && rm neo4j-community.tar.gz \
    && curl -fSL -o neo4j-2.1.5-sparql-plugin.jar https://github.com/jedivind/neo4j-sparql-extension/releases/download/1.0.0b/neo4j-sparql-extension-1.0.0.jar \
    && mv neo4j-2.1.5-sparql-plugin.jar /var/lib/neo4j/plugins/ \
    && apt-get purge -y --auto-remove curl && rm -rf /var/lib/apt/lists/* 

RUN sed -i -e "s|.*dbms.pagecache.memory=.*|dbms.pagecache.memory=512M|g" /var/lib/neo4j/conf/neo4j.properties \
    && sed -i -e "s|.*keep_logical_logs=.*|keep_logical_logs=100M size|g" /var/lib/neo4j/conf/neo4j.properties \
    && sed -i -e "s|#*remote_shell_enabled=.*|remote_shell_enabled=true|g" /var/lib/neo4j/conf/neo4j.properties \
    && sed -i -e "s|org.neo4j.server.webadmin.rrdb.location=.*|org.neo4j.server.webadmin.rrdb.location=/tmp/rrd|g" /var/lib/neo4j/conf/neo4j-server.properties \
    && sed -i -e "s|Dneo4j.ext.udc.source=.*|Dneo4j.ext.udc.source=docker|g" /var/lib/neo4j/conf/neo4j-wrapper.conf \
    && sed -i -e "s|#org.neo4j.server.thirdparty_jaxrs_classes=.*|org.neo4j.server.thirdparty_jaxrs_classes=de.unikiel.inf.comsys.neo4j=/rdf|g" /var/lib/neo4j/conf/neo4j-server.properties

VOLUME /data

COPY neo4j.sh /neo4j.sh

EXPOSE 7474 7473

CMD ["/neo4j.sh"]
