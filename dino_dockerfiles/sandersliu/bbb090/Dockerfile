#name of container: docker-bigbluebutton
#versison of container: 0.5.1
FROM sandersliu/ubuntu1410
MAINTAINER sanders liu "sandersliu@hotmail.com"

# Set correct environment variables.
ENV HOME /root
#add repository and update the container
#Installation of nesesary package/software for this containers...
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty main restricted universe multiverse" >> /etc/apt/sources.list \
&& wget http://ubuntu.bigbluebutton.org/bigbluebutton.asc -O- | sudo apt-key add - \
&& echo "deb http://ubuntu.bigbluebutton.org/trusty-090/ bigbluebutton-trusty main" >> /etc/apt/sources.list
#normally I don't like it but for this one maybe I needed it ...
RUN apt-get -y update && apt-get -y dist-upgrade
#required
RUN apt-get install -y -q language-pack-en \
&&update-locale LANG=en_US.UTF-8 \
&& dpkg-reconfigure locales

#install ffmpeg
copy ffmpeg.sh /tmp/ffmpeg.sh
RUN chmod +x /tmp/ffmpeg.sh \
&& /bin/bash -c /tmp/ffmpeg.sh

RUN apt-get update && apt-get install -y -q --force-yes openjdk-7-jdk \
tomcat7 \
&& apt-get clean \
&& rm -rf /tmp/* /var/tmp/* \
&& rm -rf /var/lib/apt/lists/*

##startup scripts
#Pre-config scrip that maybe need to be run one time only when the container run the first time .. using a flag to don't
#run it again ... use for conf for service ... when run the first time ...
RUN mkdir -p /etc/my_init.d
COPY startup.sh /etc/my_init.d/startup.sh
RUN chmod +x /etc/my_init.d/startup.sh

##Adding Deamons to containers
# to add tomcat7 deamon to runit
RUN mkdir /etc/service/tomcat7
COPY tomcat7.sh /etc/service/tomcat7/run
RUN chmod +x /etc/service/tomcat7/run
#pre-config scritp for different service that need to be run when container image is create
#maybe include additional software that need to be installed ... with some service running ... like example mysqld
COPY pre-conf.sh /sbin/pre-conf
RUN chmod +x /sbin/pre-conf \
&& /bin/bash -c /sbin/pre-conf \
&& rm /sbin/pre-conf
##scritp that can be running from the outside using docker-bash tool ...
## for example to create backup for database with convitation of VOLUME dockers-bash container_ID backup_mysql
COPY backup.sh /sbin/backup
RUN chmod +x /sbin/backup
VOLUME /var/backups
#add files and script that need to be use for this container
#include conf file relate to service/daemon
#additionsl tools to be use internally
COPY after_install.sh /sbin/after_install
RUN chmod +x /sbin/after_install
#add files and script that need to be use for this container
#include conf file relate to service/daemon
#additionsl tools to be use internally
RUN bbb-conf --enablewebrtc
# to allow access from outside of the container to the container service
# at that ports need to allow access from firewall if need to access it outside of the server.
EXPOSE 80 9123 1935 5066
#creatian of volume
#VOLUME
# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
