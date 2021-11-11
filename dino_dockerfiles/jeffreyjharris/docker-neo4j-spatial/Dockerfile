#
# Dockerizing Neo4j graph database (http://www.github.com/jeffreyjharris/docker-neo4j-spatial)
#
FROM       java:openjdk-8-jdk
MAINTAINER Jeff Harris <jeffreyjharris@mail.com>

# Install Neo4j
RUN wget -O - http://debian.neo4j.org/neotechnology.gpg.key | apt-key add - && \
    echo 'deb http://debian.neo4j.org/repo stable/' > /etc/apt/sources.list.d/neo4j.list && \
    apt-get update ; apt-get install neo4j -y

WORKDIR /var/lib/neo4j

# Copy plugins to the container — e.g., the spatial plugin
COPY plugins /var/lib/neo4j/plugins

# Copy configurations
COPY conf/neo4j /var/lib/neo4j/conf

# Copy the bootstrap shell script and set permissions
COPY sbin/bootstrap.sh /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh && \
    chmod 700 /etc/bootstrap.sh

# Customize configurations (alternatively customize conf/neo4j-server.properties before building container)
RUN apt-get clean && \
    sed -i "s|data/graph.db|/opt/data/graph.db|g" /var/lib/neo4j/conf/neo4j-server.properties && \
    sed -i "s|dbms.security.auth_enabled=true|dbms.security.auth_enabled=false|g" /var/lib/neo4j/conf/neo4j-server.properties && \
    sed -i "s|#org.neo4j.server.webserver.address|org.neo4j.server.webserver.address|g" /var/lib/neo4j/conf/neo4j-server.properties && \
#    sed -i "s|#org.neo4j.server.thirdparty_jaxrs_classes=org.neo4j.examples.server.unmanaged=/examples/unmanaged|org.neo4j.server.thirdparty_jaxrs_classes=extension=/service|g" /var/lib/neo4j/conf/neo4j-server.properties

# issue running Neo4J with RRDs under VirtualBox on OS X
# see https://www.mail-archive.com/neo4j@googlegroups.com/msg07887.html
    sed -i -e "s|org.neo4j.server.webadmin.rrdb.location=.*|org.neo4j.server.webadmin.rrdb.location=/tmp/rrd|g" /var/lib/neo4j/conf/neo4j-server.properties && \
    touch /tmp/rrd



# Expose the Neo4j browser to the host OS on port 7474, 7473 and 1337
EXPOSE 7474
EXPOSE 7473
EXPOSE 1337

# Mount a volume for persistent data
VOLUME /opt/data

# Set the bootstrap script on container run
ENV BOOTSTRAP /etc/bootstrap.sh
CMD ["/etc/bootstrap.sh", "-d"]
