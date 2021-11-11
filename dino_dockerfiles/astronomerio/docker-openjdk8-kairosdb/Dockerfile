# Dockerfile to run KairosDB on Cassandra. Configuration is done through environment variables.
#
# The following environment variables can be set
#
#     $CASS_HOSTS           [kairosdb.datastore.cassandra.host_list] (default: localhost:9160)
#                           Cassandra seed nodes (host:port,host:port)
#
#     $REPFACTOR            [kairosdb.datastore.cassandra.replication_factor] (default: 1)
#                           Desired replication factor in Cassandra
#
#     $PORT_TELNET          [kairosdb.telnetserver.port] (default: 4242)
#                           Port to bind for telnet server
#
#     $PORT_HTTP            [kairosdb.jetty.port] (default: 8080)
#                           Port to bind for http server
#
#     $PORT_CARBON_TEXT     [kairosdb.carbon.text.port] (default: 2003)
#                           Port to bind for carbon text server
#
#     $PORT_CARBON_PICKLE   [kairosdb.carbon.pickle.port] (default: 2004)
#                           Port to bind for carbon pickle server
#
#     $ENABLE_ROLLUP        [kairosdb.service.rollups] (default: unset)
#                           Enables rollups
#
# Sample Usage:
#                  docker run -P -e "CASS_HOSTS=192.168.1.63:9160" -e "REPFACTOR=1" enachb/archlinux-kairosdb

FROM openjdk:8
MAINTAINER ken@astronomer.io.io

EXPOSE 8080
EXPOSE 4242
EXPOSE 2003
EXPOSE 2004

ENV KAIROSDB_VERSION=1.1.3
ENV KAIROS_CARBON_VERSION=1.1

# Install gettext
RUN apt-get update && apt-get install -y gettext

# Install KAIROSDB
RUN cd /opt; \
  curl -L https://github.com/kairosdb/kairosdb/releases/download/v${KAIROSDB_VERSION}/kairosdb-${KAIROSDB_VERSION}-1.tar.gz | \
  tar zxfp - && \
  curl -L https://github.com/kairosdb/kairos-carbon/releases/download/v${KAIROS_CARBON_VERSION}-1/kairos-carbon-${KAIROS_CARBON_VERSION}.tar.gz | \
  tar zxfp -

# Clean up APT when done.
RUN apt-get autoremove
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD kairosdb.properties /tmp/kairosdb.properties
ADD runKairos.sh /usr/bin/runKairos.sh

# Run kairosdb in foreground on boot
ENTRYPOINT [ "/usr/bin/runKairos.sh" ]
