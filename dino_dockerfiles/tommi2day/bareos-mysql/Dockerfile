FROM       ubuntu:trusty
MAINTAINER Tommi2Day

ENV DEBIAN_FRONTEND noninteractive
ENV HOSTNAME bareos
ENV TERM linux

#install standard packages
RUN apt-get update && apt-get install -y wget aptitude mysql-server apache2 postfix ntpdate

#install bareos from there own repo
RUN bash -c 'echo "deb http://download.bareos.org/bareos/release/latest/xUbuntu_14.04/ /" > /etc/apt/sources.list.d/bareos.list'
RUN bash -c 'wget -q http://download.bareos.org/bareos/release/latest/xUbuntu_14.04/Release.key -O- | apt-key add -'
RUN apt-get update && apt-get install -y bareos bareos-database-mysql bareos-webui 

#clean
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

#save default configs
RUN tar cfvz /etc.tgz /etc/bareos /etc/bareos-webui 

#Mountpoints
RUN mkdir -p /db /backup

#add scripts
ADD prepare.sh /prepare.sh
ADD start.sh /start.sh
ADD configure.sh /configure.sh
RUN chmod u+x /*.sh
RUN /configure.sh

#volumes
VOLUME ["/db","/var/log/mysql"]
VOLUME ["/backup"]
VOLUME ["/etc/bareos","/var/log/bareos","/etc/bareos-webui"]
VOLUME ["/var/log/apache2"]

# web, director, fd, storage, mysql daemons 
EXPOSE 80 9101 9102 9103 3306

ENTRYPOINT ["/prepare.sh"]
CMD ["/start.sh"]

