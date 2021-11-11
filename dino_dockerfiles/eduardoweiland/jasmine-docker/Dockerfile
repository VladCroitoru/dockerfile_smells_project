# Dockerfile baseado no QuantumObject/docker-cacti

FROM quantumobject/docker-baseimage:15.10
MAINTAINER Eduardo Weiland "eduardo@eduardoweiland.info"

#add repository and update the container
#Installation of nesesary package/software for this containers...
RUN echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc)-backports main restricted " >> /etc/apt/sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) multiverse " >> /etc/apt/sources.list
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
        snmpd snmp-mibs-downloader \
        apache2 php5 php5-intl php5-snmp php5-mysql \
        mysql-server \
        unzip
RUN mysql_install_db > /dev/null 2>&1 \
    && touch /var/lib/mysql/.EMPTY_DB \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

##startup scripts
#Pre-config scrip that maybe need to be run one time only when the container run the first time .. using a flag to don't
#run it again ... use for conf for service ... when run the first time ...
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

##Adding Deamons to containers
# to add apache2 deamon to runit
RUN mkdir /etc/service/apache2
COPY apache2.sh /etc/service/apache2/run
RUN chmod +x /etc/service/apache2/run

# to add mysqld deamon to runit
RUN mkdir /etc/service/mysqld
COPY mysqld.sh /etc/service/mysqld/run
RUN chmod +x /etc/service/mysqld/run

# to add snmpd deamon to runit
RUN mkdir /etc/service/snmpd
COPY snmpd.sh /etc/service/snmpd/run
RUN chmod +x /etc/service/snmpd/run

#pre-config script for different service that need to be run when container image is create 
#maybe include additional software that need to be installed ... with some service running ... like example mysqld
COPY pre-conf.sh /sbin/pre-conf
RUN chmod +x /sbin/pre-conf \
    && /bin/bash -c /sbin/pre-conf \
    && rm /sbin/pre-conf


#add files and script that need to be use for this container
#include conf file relate to service/daemon
#additional tools to be use internally
COPY snmpd.conf /etc/snmp/snmpd.conf
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

# to allow access from outside of the container  to the container service
# at that ports need to allow access from firewall if need to access it outside of the server.
EXPOSE 80 161

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

