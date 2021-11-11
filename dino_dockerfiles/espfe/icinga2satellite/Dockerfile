## Dockerfile for espfe/icinga2_satellite
## https://github.com/ESPFE/icinga2_satellite
## https://www.edv-peuker.de

## DANGER ##
## Before up- or downgrade the debian version check the file ./conf/etc/apt/sources.list
FROM debian:buster

MAINTAINER André Sünnemann - EDV-Systeme Peuker GmbH & Co. KG <a.suennemann@edv-peuker.de>

LABEL version="1.2.0"

## update /etc/apt/sources.list
RUN rm /etc/apt/sources.list
COPY config/etc/apt/sources.list /etc/apt/sources.list

RUN apt-get update \
	&& apt-get dist-upgrade -y \
	&& apt-get install -y \
		curl \
		apt-transport-https \
		bash \
		gnupg \
		supervisor \
		bc \
		libnet-snmp-perl \
		libsnmp-perl \
		coreutils
		
RUN curl -s https://packages.icinga.com/icinga.key \
	| apt-key add -
RUN echo 'deb http://packages.icinga.com/debian icinga-buster main' \
	> /etc/apt/sources.list.d/icinga.list

RUN apt-get update \
	&& apt-get install -y icinga2 \
	monitoring-plugins \
	monitoring-plugins-basic \
	nagios-plugins-contrib \
	monitoring-plugins-standard \
	snmp-mibs-downloader
		
RUN apt-get clean
RUN download-mibs
RUN rm -rf /etc/icinga2/conf.d/*
## delete wrong snmp file
RUN rm /var/lib/snmp/mibs/ietf/SNMPv2-PDU
COPY ./config/ /

RUN echo 'include_recursive "/opt/icinga2/conf.d"' >> /etc/icinga2/icinga2.conf
RUN echo 'const CustomPluginDir = "/opt/icinga2/plugins"' >> /etc/icinga2/constants.conf
RUN ln -s /usr/bin/basename /bin/basename

EXPOSE 5665

CMD ["/opt/start.sh"]
