# Dockerfile to build an image of the Kamailio SIP Server
#   Input: HOST_IP - the IP of the host that the Kamailio Server will run on.
#
FROM ubuntu:16.04

# MySQL installation configuration for root password
RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections

# Install the required packages
RUN apt-get update \
 && apt-get install -y wget
RUN wget -O- http://deb.kamailio.org/kamailiodebkey.gpg | apt-key add -
RUN echo "deb http://deb.kamailio.org/kamailio50 xenial main" >> /etc/apt/sources.list
RUN apt-get update \
 && apt-get install -y mysql-server kamailio kamailio-mysql-modules

# MySQL root user configuration
RUN echo "[client]" >> /etc/mysql/my.cnf \
 && echo "user=root\npassword=root" >> /etc/mysql/my.cnf

# Startup script to run the servers
ADD startup /root/startup

# Kamailio configuration
RUN echo "SIP_DOMAIN=sipserver.automated.test" >> /etc/kamailio/kamctlrc \
 && echo "DBENGINE=MYSQL" >> /etc/kamailio/kamctlrc \
 && echo "DBRWUSER=root" >> /etc/kamailio/kamctlrc \
 && echo "DBRWPW=root" >> /etc/kamailio/kamctlrc \
 && echo "DBROUSER=root" >> /etc/kamailio/kamctlrc \
 && echo "DBROPW=root" >> /etc/kamailio/kamctlrc \
 && echo "INSTALL_EXTRA_TABLES=yes" >> /etc/kamailio/kamctlrc \
 && echo "INSTALL_PRESENCE_TABLES=yes" >> /etc/kamailio/kamctlrc \
 && echo "INSTALL_DBUID_TABLES=yes" >> /etc/kamailio/kamctlrc

RUN /etc/init.d/mysql start \
 && kamdbctl create

RUN sed -i '/#!KAMAILIO/a #!define WITH_MYSQL\n#!define WITH_USRLOCDB' /etc/kamailio/kamailio.cfg \
 && sed -i 's/kamailio:kamailiorw/root:root/' /etc/kamailio/kamailio.cfg

RUN echo "RUN_KAMAILIO=yes" >> /etc/default/kamailio

# Configure listening ports and set the IP of the host
ARG HOST_IP
RUN sed -i "s/# listen=udp:10.0.0.10:5060/listen=udp:0.0.0.0:5060 advertise ${HOST_IP}:5060/" /etc/kamailio/kamailio.cfg

EXPOSE 5060

# Start the services
CMD /root/startup/start.sh


