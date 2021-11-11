# dhcp server: isc-dhcp-server
FROM quantumobject/docker-baseimage:16.04
MAINTAINER Tim Chaubet "tim@chaubet.be"

# Freenas container metadata - volumes defined here are created BEFORE container start
LABEL description="This image is used to launch the isc-dhcp-server service" \
      maintainer="tim@chaubet.be" \
      org.freenas.interactive="false" \
      org.freenas.version="0.23" \
      org.freenas.privileged="false" \
      org.freenas.upgradeable="true" \
      org.freenas.bridged="true" \
      org.freenas.dhcp="false" \
      org.freenas.expose-ports-at-host="true" \
      org.freenas.autostart="true" \
      org.freenas.port-mappings="67:67/udp,68:68/udp,520:520/tcp,520:520/udp" \
      org.freenas.settings="[ \
          { \
              \"env\": \"TZ\",						\
              \"descr\": \"Timezone - eg Europe/London\",		\
              \"optional\": false					      \
          } \		
      ]" \
      org.freenas.volumes="[ \
          { \
              \"name\": \"/config\", \
              \"descr\": \"Config storage space\" \
          } \
      ]" 

#add repository and update the container
#Installation of nesesary package/software for this containers...
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y isc-dhcp-server \
                       ntp \
                       ntpdate \
                       net-tools \
                       iputils-ping \
                       vim \
                       openssh-server \
 && apt-get autoclean -y \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/* /var/tmp/* 

# add dhcpd daemon to runit
RUN mkdir -p /etc/service/dhcpd /var/log/dhcpd ; sync
COPY dhcpd.sh /etc/service/dhcpd/run
RUN chmod +x /etc/service/dhcpd/run \
    && cp /var/log/cron/config /var/log/dhcpd/ 
    
# add ntp deamon to runit
RUN mkdir -p /etc/service/ntp /var/log/ntp ; sync 
COPY ntp.sh /etc/service/ntp/run
RUN chmod +x /etc/service/ntp/run \
    && cp /var/log/cron/config /var/log/ntp/ \
    && chown -R nobody /var/log/ntp
    
# add openssh-server daemon to runit
RUN mkdir -p /etc/service/sshd /var/log/sshd ; sync
COPY sshd.sh /etc/service/sshd/run
RUN chmod +x /etc/service/sshd/run \
    && cp /var/log/cron/config /var/log/sshd/ 
    
# copy dhcp config files
COPY dhcpd.conf /tmp/dhcpd.conf
COPY dhcpd.conf.synced /tmp/dhcpd.conf.synced
ADD dhcpd.conf /tmp/
ADD dhcpd.conf.synced /tmp/

### startup scripts ###

#Pre-config scrip that maybe need to be run one time only when the container run the first time .. using a flag to don't 
#run it again ... use for conf for service ... when run the first time ...
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh
    
# the normal syntax does not work: VOLUME ["/var/lib/dhcp", "/etc/dhcp", "/scripts"]
# volumes defined here are created AT container start
#VOLUME /var/test

# expose ports
#EXPOSE 67/udp
#EXPOSE 68/udp
#EXPOSE 520

RUN echo "!/bin/sh ntpdate 0.europe.pool.ntp.org" >> /etc/cron.daily/ntpdate \
    && chmod 750 /etc/cron.daily/ntpdate

CMD ["/sbin/my_init"]
