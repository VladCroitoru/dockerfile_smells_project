#name of container: mywebsql-flex
#versison of container: 0.2.3.x
FROM quantumobject/docker-baseimage:15.10
MAINTAINER Jay Watts "cysix928@gmail.com"

#add repository and update the container
#Installation of nesesary package/software for this containers...
RUN apt-get update && apt-get install -y -q unzip \
                                            php5 \
                                            apache2 \
                                            php5-mysql \
                                            php5-pgsql \
                                            php5-curl \
                                            php5-gmp \
                                            php5-sqlite\
                                            vim\
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
# to add apache2 deamon to runit
RUN mkdir -p /etc/service/apache2  /var/log/apache2 ; sync 
COPY apache2.sh /etc/service/apache2/run
RUN chmod +x /etc/service/apache2/run \
    && cp /var/log/cron/config /var/log/apache2/ \
    && chown -R www-data /var/log/apache2


#pre-config scritp for different service that need to be run when container image is create 
#maybe include additional software that need to be installed ... with some service running ... like example mysqld
COPY pre-conf.sh /sbin/pre-conf
RUN chmod +x /sbin/pre-conf; sync \
    && /bin/bash -c /sbin/pre-conf \
    && rm /sbin/pre-conf

#add files and script that need to be use for this container
#include conf file relate to service/daemon 
#additionsl tools to be use internally 
COPY apache2.conf /etc/apache2/apache2.conf

# to allow access from outside of the container  to the container service
# at that ports need to allow access from firewall if need to access it outside of the server. 
EXPOSE 80

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
