# Dockerfile to run KairosDB on Cassandra. Configuration is done through environment variables.
#
# The following environment variables can be set
#
#     $CASS_HOSTS           [kairosdb.datastore.cassandra.host_list] (default: localhost:9160)
#                           Cassandra seed nodes (host:port,host:port)
#
#     $REP_FACTOR            [kairosdb.datastore.cassandra.replication_factor] (default: 1)
#                           Desired replication factor in Cassandra
#
#     $PORT_TELNET          [kairosdb.telnetserver.port] (default: 4242)
#                           Port to bind for telnet server
#
#     $PORT_HTTP            [kairosdb.jetty.port] (default: 8083)
#                           Port to bind for http server
#
# Sample Usage:
#   docker run -P -e "CASS_HOSTS=192.168.1.63:9160" -e "REP_FACTOR=1" acconsta/kairosdb


# Oracle JDK8 on top of ubuntu
FROM n3ziniuka5/ubuntu-oracle-jdk:14.04-JDK8

MAINTAINER acconsta

# Install Kairosdb
ADD https://github.com/kairosdb/kairosdb/releases/download/v1.0.0/kairosdb_1.0.0-1_all.deb .
RUN dpkg -i kairosdb_1.0.0-1_all.deb 

# Install envsubst
RUN apt-get update && \
    apt-get install -y gettext

ADD kairosdb.properties /tmp/kairosdb.properties
ADD run_kairos.sh /usr/bin/run_kairos.sh
RUN chmod +x /usr/bin/run_kairos.sh

# Kairos API telnet and jetty ports
EXPOSE 4242 8083

# Run kairosdb in foreground on boot
ENTRYPOINT ["/usr/bin/run_kairos.sh"]
