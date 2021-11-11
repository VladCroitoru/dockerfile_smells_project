FROM ubuntu:trusty
MAINTAINER Patrick McClory <pmcclory@gmail.com>

RUN \ 
	echo 'deb http://www.ubnt.com/downloads/unifi/distros/deb/ubuntu ubuntu ubiquiti' >> /etc/apt/sources.list && \ 
	apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50 && \
	apt-get update -y && \ 
	apt-get install -y unifi-beta

CMD ["service unifi stop && service unifi start && tail -f /var/log/unifi/server.log"]

#Expose external ports per https://community.ubnt.com/t5/UniFi-Controller-Installation/UniFi-Change-default-ports-for-controller-and-UAPs/ta-p/412673
EXPOSE 8081 8080 8443 8880 8843
