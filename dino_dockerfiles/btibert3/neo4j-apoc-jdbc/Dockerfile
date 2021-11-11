# Insipred by https://github.com/CliffordAnderson/docker-containers/blob/master/neo4j/Dockerfile
# Includes JDBC plugins
# https://neo4j.com/developer/kb/how-do-i-use-cypher-to-connect-to-a-rbms-using-jdbc/

FROM neo4j:3.5.3
MAINTAINER Brock Tibert <btibert3@gmail.com>

ENV APOC_URI https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/3.5.0.2/apoc-3.5.0.2-all.jar
ENV POSTGRES_URI https://jdbc.postgresql.org/download/postgresql-9.4.1209.jar


RUN mv plugins /plugins && ln -s /plugins

RUN curl --fail --silent --show-error --location --output apoc-3.5.0.2-all.jar $APOC_URI \
    && mv apoc-3.5.0.2-all.jar /plugins

RUN curl --fail --silent --show-error --location --output postgresql-9.4.1209.jar $POSTGRES_URI \
    && mv postgresql-9.4.1209.jar /plugins

EXPOSE 7474 7473 7687

CMD ["neo4j"]
