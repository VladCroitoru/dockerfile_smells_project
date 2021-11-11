FROM debian:jessie
MAINTAINER Erik Kellener [erik@kellener.com]

# apt netatalk
# Add Java 8
RUN echo "deb http://ftp.de.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN apt-get update && \
 apt-get -y install  git zip unzip screen avahi-daemon wget

#For debugging
RUN apt-get install nano

RUN apt install -y -t jessie-backports  openjdk-8-jre-headless ca-certificates-java
RUN mkdir /data 
#VOLUME /data
WORKDIR /data

#Build Spigot
RUN cd /data && \
wget -O /data/BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar  && \
java -jar BuildTools.jar


RUN mkdir -p /data/config
COPY minecraft.sh /data/minecraft.sh
COPY spigot.yml /data/spigot.yml

# script that finds UUID (used to populate ops.json
COPY lookupuuid.sh /data/lookupuuid.sh
RUN chmod +x /data/minecraft.sh

RUN tar -cvf /data.tar /data/* 
#Edit spigot.yml Set view-distance: 5.
#RUN sed -i 's/view-distance: 10/view-distance: 5/g' /data/spigot.yml


#Update /etc/rc.local and add  su -l pi -c /data/minecraft.sh 
RUN echo "su -l -c /data/minecraft.sh" >> /etc/rc.local 


#If not already set up
#edit /etc/default/tmpfs ensure RAMTMP=yes

ENV PATH="/:${PATH}"

#Other default port is (25565) Ensure this is open
EXPOSE 25565/tcp

# Start the service
ENTRYPOINT ["/bin/bash","minecraft.sh"]


#Reference
#https://www.dropbox.com/install-linux
#http://lemire.me/blog/2016/04/02/setting-up-a-robust-minecraft-server-on-a-raspberry-pi/


 
