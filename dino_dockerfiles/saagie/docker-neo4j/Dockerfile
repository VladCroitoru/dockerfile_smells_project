FROM neo4j:3.3

MAINTAINER Saagie

RUN cp -R /data /data-neo4j \
    && chown -R neo4j:neo4j /data-neo4j \
    && chmod -R 777 /data-neo4j \
    && chown -R neo4j:neo4j /var/lib/neo4j \
    && chmod -R 777 /var/lib/neo4j \
    && rm -f /var/lib/neo4j/data \
    && ln -s /data-neo4j /var/lib/neo4j/data

VOLUME /data-neo4j

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh
