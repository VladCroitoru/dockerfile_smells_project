FROM openjdk

ENV cassandra_loader_version=v0.0.25

RUN wget https://github.com/brianmhess/cassandra-loader/releases/download/${cassandra_loader_version}/cassandra-loader -O /usr/local/bin/cassandra-loader && \
    wget https://github.com/brianmhess/cassandra-loader/releases/download/${cassandra_loader_version}/cassandra-unloader -O /usr/local/bin/cassandra-unloader && \
    chmod +x /usr/local/bin/cassandra-* 
