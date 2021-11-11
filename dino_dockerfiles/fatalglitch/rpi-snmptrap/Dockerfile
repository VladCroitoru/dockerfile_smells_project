FROM ubuntu:xenial
MAINTAINER fatalglitch82

EXPOSE 162

RUN apt-get update && \
    apt-get install -y snmpd snmptrapd snmptt snmp-mibs-downloader && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sed -i s_TRAPDRUN=no_TRAPDRUN=yes_g /etc/default/snmptrapd

VOLUME ["/etc/snmp"]

CMD ["snmptrapd", "-f" ]
