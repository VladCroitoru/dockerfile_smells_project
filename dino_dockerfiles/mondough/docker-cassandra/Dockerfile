# Spotify Cassandra 2.1.8 Single Node Image
#
# VERSION               0.1
#
# Starts a Cassandra instance constituting a one node cluster.

FROM java:7

ENV DEBIAN_FRONTEND noninteractive

# Add DataStax sources
RUN curl -L http://debian.datastax.com/debian/repo_key | apt-key add -
RUN echo "deb http://debian.datastax.com/community stable main" | tee -a /etc/apt/sources.list.d/cassandra.sources.list

# Workaround for https://github.com/docker/docker/issues/6345
RUN ln -s -f /bin/true /usr/bin/chfn

# Install Cassandra 2.1.8
RUN apt-get update && \
    apt-get install -y --force-yes cassandra=2.1.8 dsc21=2.1.8-1 && \
    rm -rf /var/lib/apt/lists/*

ENV CASSANDRA_CONFIG /etc/cassandra

# Run base config script
ADD scripts/config-cassandra-base.sh /usr/local/bin/config-cassandra-base
RUN /usr/local/bin/config-cassandra-base

# Necessary since cassandra is trying to override the system limitations
# See https://groups.google.com/forum/#!msg/docker-dev/8TM_jLGpRKU/dewIQhcs7oAJ
RUN rm -f /etc/security/limits.d/cassandra.conf

EXPOSE 7199 7000 7001 9160 9042 22 8012 61621

CMD [""]


# Everything before this line was originally in spotify/docker-cassandra:base
# Everything past this line was originally in spotify/docker-cassandra

# Place single-node startup-config script
ADD scripts/cassandra-singlenode.sh /usr/local/bin/cassandra-singlenode

# Start Cassandra
ENTRYPOINT ["cassandra-singlenode"]
