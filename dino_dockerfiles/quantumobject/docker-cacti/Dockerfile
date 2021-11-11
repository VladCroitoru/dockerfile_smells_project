#name of container: docker-cacti
#versison of container: 0.6.4
FROM quantumobject/docker-baseimage:18.04
MAINTAINER Angel Rodriguez  "angel@quantumobject.com"

ENV TZ America/New_York

# Update the container
#Installation of nesesary package/software for this containers...
RUN apt-get update && echo $TZ > /etc/timezone && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends mariadb-server mariadb-client php build-essential automake \
                                                            apache2 snmp libapache2-mod-php libssl-dev vim \
                                                            rrdtool librrds-perl php-mysql php-pear \
                                                            php-common php-json php-gettext libtool \
                                                            php-pspell php-recode php-tidy php-xmlrpc \
                                                            php-xml php-ldap php-mbstring php-intl \
                                                            php-gd php-snmp php-gmp php-curl php-net-socket\
                                                            libmysqlclient-dev libsnmp-dev dos2unix help2man git \
                                                            snmpd python-netsnmp libnet-snmp-perl snmp-mibs-downloader \
                                                            iputils-ping autoconf unzip \
                    && cd /opt/ \
                    && wget https://www.cacti.net/downloads/cacti-latest.tar.gz \
                    && ver=$(tar -tf cacti-latest.tar.gz | head -n1 | tr -d /) \
                    && tar -xvf cacti-latest.tar.gz && mv $ver cacti \
                    && rm cacti-latest.tar.gz \
                    && apt-get clean \
                    && rm -rf /tmp/* /var/tmp/*  \
                    && rm -rf /var/lib/apt/lists/*

# Ensure cron is allowed to run
RUN sed -i 's/^\(session\s\+required\s\+pam_loginuid\.so.*$\)/# \1/g' /etc/pam.d/cron

##Get Mibs
RUN /usr/bin/download-mibs
RUN echo 'mibs +ALL' >> /etc/snmp/snmp.conf
## fix prblem with mibs downloader and ubuntu 18.04
RUN rm /usr/share/snmp/mibs/ietf/IPSEC-SPD-MIB \
    && rm /usr/share/snmp/mibs/ietf/IPATM-IPMC-MIB \
    && rm /usr/share/snmp/mibs/iana/IANA-IPPM-METRICS-REGISTRY-MIB \
    && rm /usr/share/snmp/mibs/ietf/SNMPv2-PDU

##startup scripts
#Pre-config scrip that maybe need to be run one time only when the container run the first time .. using a flag to don't
#run it again ... use for conf for service ... when run the first time ...
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

##Adding Deamons to containers
# to add apache2 deamon to runit
RUN mkdir -p /etc/service/apache2  /var/log/apache2 ; sync
COPY apache2.sh /etc/service/apache2/run
RUN chmod +x /etc/service/apache2/run  \
    && cp /var/log/cron/config /var/log/apache2/ \
    && chown -R www-data /var/log/apache2

# to add mysqld deamon to runit
RUN mkdir -p /etc/service/mysqld /var/log/mysqld ; sync
COPY mysqld.sh /etc/service/mysqld/run
RUN chmod +x /etc/service/mysqld/run  \
    && cp /var/log/cron/config /var/log/mysqld/ \
    && chown -R mysql /var/log/mysqld

# to add mysqld deamon to runit
RUN mkdir -p /etc/service/snmpd /var/log/snmpd ; sync
COPY snmpd.sh /etc/service/snmpd/run
RUN chmod +x /etc/service/snmpd/run  \
   && cp /var/log/cron/config /var/log/snmpd/ \
   && chown -R Debian-snmp /var/log/snmpd

#add files and script that need to be use for this container
#include conf file relate to service/daemon
#additionsl tools to be use internally
COPY snmpd.conf /etc/snmp/snmpd.conf
COPY debian.conf /opt/cacti/include/config.php
COPY spine.conf /usr/local/spine/etc/spine.conf

#pre-config scritp for different service that need to be run when container image is create
#maybe include additional software that need to be installed ... with some service running ... like example mysqld
COPY pre-conf.sh /sbin/pre-conf
RUN chmod +x /sbin/pre-conf ; sync \
    && /bin/bash -c /sbin/pre-conf \
    && rm /sbin/pre-conf

# Volume for container   
VOLUME /opt/cacti/plugins /var/log /opt/cacti/templates /var/lib/mysql /opt/cacti/rra


# to allow access from outside of the container  to the container service
# at that ports need to allow access from firewall if need to access it outside of the server.
EXPOSE 80

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
