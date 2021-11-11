#name of container: docker-tor-exit-relay
#versison of container: 0.6.0
FROM quantumobject/docker-baseimage:18.04
MAINTAINER Angel Rodriguez  "angel@quantumobject.com"

ENV Nickname TorRelayNickName

# Update the container
# Installation of nesesary package/software for this containers...
RUN echo "deb http://deb.torproject.org/torproject.org `cat /etc/container_environment/DISTRIB_CODENAME` main" >> /etc/apt/sources.list
RUN wget https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc
RUN DEBIAN_FRONTEND=noninteractive apt-key add <A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc
RUN apt-get update && apt-get install -y -q tor tor-arm tor-geoipdb \
                    openntpd apt-transport-https \
                    deb.torproject.org-keyring \
                    openssh-server \
                    lynx fail2ban \
                    && apt-get clean \
                    && rm -rf /tmp/* /var/tmp/*  \
                    && rm -rf /var/lib/apt/lists/*

##startup scripts  
#Pre-config scrip that maybe need to be run one time only when the container run the first time .. using a flag to don't 
#run it again ... use for conf for service ... when run the first time ...
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

##Adding Deamons to containers
RUN mkdir -p /etc/service/tor /var/log/tor ; sync
COPY tor.sh /etc/service/tor/run
RUN chmod +x /etc/service/tor/run \
     && cp /var/log/cron/config /var/log/tor/
     
RUN mkdir -p /etc/service/sshd /var/log/sshd ; sync 
COPY sshd.sh /etc/service/sshd/run
RUN chmod +x /etc/service/sshd/run \
    && cp /var/log/cron/config /var/log/sshd      
    
RUN mkdir -p /etc/service/fail2ban /var/log/fail2ban /var/run/fail2ban ; sync 
COPY fail2ban.sh /etc/service/fail2ban/run
RUN chmod +x /etc/service/fail2ban/run \
    && touch /var/log/auth.log \
    && cp /var/log/cron/config /var/log/fail2ban 

#add files and script that need to be use for this container
#include conf file relate to service/daemon 
#additionsl tools to be use internally 
COPY torrc /etc/tor/torrc
RUN mkdir -p /var/www ; sync 
COPY tor-exit-notice.html /var/www/tor-exit-notice.html
RUN mkdir -p /var/run/sshd

# to allow access from outside of the container  to the container service
# at that ports need to allow access from firewall if need to access it outside of the server. 
EXPOSE 22 9050 9001 80

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
