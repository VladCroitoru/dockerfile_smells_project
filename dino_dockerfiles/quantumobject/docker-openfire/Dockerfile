#name of container: docker-openfire
#versison of container: 0.3.3
FROM quantumobject/docker-baseimage:18.04
MAINTAINER Angel Rodriguez  "angel@quantumobject.com"

#add repository and update the container
#Installation of nesesary package/software for this containers...
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q --no-install-recommends openjdk-8-jdk \
                    && apt-get clean \
                    && apt-get autoremove \
                    && rm -rf /tmp/* /var/tmp/*  \
                    && rm -rf /var/lib/apt/lists/*

##startup scripts  
#Pre-config scrip that maybe need to be run one time only when the container run the first time .. using a flag to don't 
#run it again ... use for conf for service ... when run the first time ...
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

##Adding Deamons to containers
# to add openfire deamon to runit
RUN mkdir /etc/service/openfire
COPY openfire.sh /etc/service/openfire/run
RUN chmod +x /etc/service/openfire/run 

#pre-config scritp for different service that need to be run when container image is create 
#maybe include additional software that need to be installed ... with some service running ... like example mysqld
COPY pre-conf.sh /sbin/pre-conf
RUN chmod +x /sbin/pre-conf; sync \
    && /bin/bash -c /sbin/pre-conf \
    && rm /sbin/pre-conf

# to allow access from outside of the container  to the container service
# at that ports need to allow access from firewall if need to access it outside of the server. 
EXPOSE 7070 7443 7777 9090 9091 5000-6000/udp 5000-6000/tcp

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
