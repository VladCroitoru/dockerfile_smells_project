FROM java:8-jdk

ENV CASSANDRA_VER 1.1.12

RUN wget http://archive.apache.org/dist/cassandra/${CASSANDRA_VER}/apache-cassandra-${CASSANDRA_VER}-bin.tar.gz && \
    tar xvzf apache-cassandra-${CASSANDRA_VER}-bin.tar.gz -C /srv/ && \
    mv /srv/apache-cassandra-${CASSANDRA_VER} /srv/cassandra && \
    rm -f apache-cassandra-${CASSANDRA_VER}-bin.tar.gz
ADD conf/cassandra-env.sh /srv/cassandra/conf/

EXPOSE 7000 7001 7199 9042 9160
ENTRYPOINT ["/srv/cassandra/bin/cassandra", "-f"]