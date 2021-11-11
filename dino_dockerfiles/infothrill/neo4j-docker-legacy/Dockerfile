FROM java:openjdk-8-jre

RUN apt-get update --quiet --quiet \
    && apt-get install --quiet --quiet --no-install-recommends lsof \
    && rm -rf /var/lib/apt/lists/*

ENV NEO4J_SHA256 faf209dbeef9851c88717660a4b7ccb5110343a9ed53110f516b675c8230c39a
ENV NEO4J_VERSION 2.1.8
ENV NEO4J_TARBALL neo4j-community-$NEO4J_VERSION-unix.tar.gz
ENV NEO4J_URI=http://dist.neo4j.org/neo4j-community-$NEO4J_VERSION-unix.tar.gz

RUN curl --fail --silent --show-error --location --remote-name ${NEO4J_URI} \
    && echo "${NEO4J_SHA256} ${NEO4J_TARBALL}" | sha256sum --check --quiet - \
    && tar --extract --file ${NEO4J_TARBALL} --directory /var/lib \
    && mv /var/lib/neo4j-* /var/lib/neo4j \
    && rm ${NEO4J_TARBALL}

WORKDIR /var/lib/neo4j

RUN mv data /data \
    && ln --symbolic /data

VOLUME /data

COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY trap.sh /trap.sh
COPY initneo4j.sh /initneo4j.sh

EXPOSE 7474 7473

ENTRYPOINT ["/initneo4j.sh"]
CMD ["neo4j"]
