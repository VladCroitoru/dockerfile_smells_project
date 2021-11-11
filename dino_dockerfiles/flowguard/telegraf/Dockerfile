FROM telegraf:1.20
LABEL maintainer="jaroslav.barton@comsource.cz"

ADD sources.list /etc/apt/

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends snmp-mibs-downloader && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /tmp/juniper && \
    cd /tmp/juniper && \
    curl -L -O "https://www.juniper.net/documentation/software/junos/junos182/juniper-mibs-18.2R1.9-signed.tgz" && \
    tar xvf juniper-mibs-18.2R1.9-signed.tgz && \
    tar xvf juniper-mibs-18.2R1.9.tgz && \
    cp JuniperMibs/* /usr/share/snmp/mibs/ && \
    rm -rf /tmp/juniper

ADD IF-MIB /var/lib/snmp/mibs/ietf/IF-MIB
