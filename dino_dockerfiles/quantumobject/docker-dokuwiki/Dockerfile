#name of container: docker-dokuwiki
#versison of container: 0.3.3
FROM quantumobject/docker-baseimage:18.04
MAINTAINER Angel Rodriguez  "angel@quantumobject.com"

#add repository and update the container
#Installation of nesesary package/software for this containers...
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q --no-install-recommends apache2 libapache2-mod-php \
                    php php-xml php-mbstring\
                    && cd /var/www   \
                    && wget http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz \
                    && tar xvf dokuwiki-stable.tgz \
                    && rm dokuwiki-stable.tgz \
                    && mv dokuwiki-* dokuwiki \
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

#script to execute after install configuration done ....
COPY after_install.sh /sbin/after_install
RUN chmod +x /sbin/after_install

#add files and script that need to be use for this container
#include conf file relate to service/daemon 
#additionsl tools to be use internally
COPY apache2.conf /etc/apache2/apache2.conf

VOLUME /var/www/dokuwiki/conf  /var/www/dokuwiki/data
# to allow access from outside of the container  to the container service
# at that ports need to allow access from firewall if need to access it outside of the server. 
EXPOSE 80

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
