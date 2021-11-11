FROM telco2011/ubuntu-oracle-java:14.10jre7u80
MAINTAINER David Lopez <davidlopez.david@gmail.com>

# Download and start neo4j
RUN mkdir /soft
WORKDIR /soft
RUN wget http://dist.neo4j.org/neo4j-community-2.2.1-unix.tar.gz
RUN tar zxvf neo4j-community-2.2.1-unix.tar.gz
RUN ln -s /soft/neo4j-community-2.2.1 /soft/neo4j

# Configure host access
RUN sed -i "s|#org.neo4j.server.webserver.address=0.0.0.0|org.neo4j.server.webserver.address=0.0.0.0|g" /soft/neo4j/conf/neo4j-server.properties

# Expose the ports we're interested in
EXPOSE 7474 1337

# Start Neo4j
CMD ["/soft/neo4j/bin/neo4j", "console"]