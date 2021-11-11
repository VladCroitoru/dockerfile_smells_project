FROM zabbix/zabbix-server-mysql:ubuntu-5.0-latest

MAINTAINER Dirk Steinkopf "https://github.com/dsteinkopf"

USER root

# enable the multiverse (snmp-mibs-downloader comes from there)
RUN echo 'deb http://archive.ubuntu.com/ubuntu/ bionic multiverse' >> /etc/apt/sources.list && \
    echo 'deb http://archive.ubuntu.com/ubuntu/ bionic-updates multiverse' >> /etc/apt/sources.list && \
    echo 'deb http://archive.ubuntu.com/ubuntu/ bionic-security multiverse' >> /etc/apt/sources.list

# bc is for some externalscripts (e.g. zext_ssl_cert.sh)

RUN apt-get update && \
        apt-get -y dist-upgrade && \
        apt-get -y autoremove && \
        apt-get clean && \
        apt-get install -y \
                bc \
                curl \
                python3-pip \
		snmp \
		snmp-mibs-downloader \
                jq \
                curl \
		freeradius-utils \
		bind9-host

# seems important for mib lookup to work:
ENV MIBDIRS=/var/lib/snmp/mibs/ietf:/var/lib/snmp/mibs/iana:/usr/share/snmp/mibs:/var/lib/zabbix/mibs

# enable snmp mibs loading:
# remove problematic mibs which result in errors and are not needed (...why is this necessary?...)
RUN sed -i 's/^\( *mibs *:.*\)$/# \1/g' /etc/snmp/snmp.conf && \
	rm -f /var/lib/snmp/mibs/ietf/SNMPv2-PDU && \
	snmptranslate .iso.3.6.1.6.3.1.1.5.3

RUN pip3 install requests

RUN sed -i 's/update_config_var .ZBX_CONFIG .Fping6Location./update_config_var $ZBX_CONFIG "Fping6Location" "\/doesnotexist"/' /usr/bin/docker-entrypoint.sh
RUN sed -i 's/update_config_var .ZBX_CONFIG .FpingLocation./update_config_var $ZBX_CONFIG "FpingLocation" "\/usr\/bin\/fping"/' /usr/bin/docker-entrypoint.sh

USER 1997
