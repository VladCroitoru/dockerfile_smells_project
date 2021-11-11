FROM ubuntu:18.04
MAINTAINER Henry Southgate

ENV DEBIAN_FRONTEND noninteractive

# Install mongodb and UniFi sources
COPY apt/ /etc/apt/

# Install the UniFi GPG key
# RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50 

# Install CA certs
RUN apt-get -y update && \
    apt-get -y install ca-certificates apt-transport-https && \
	rm -rf /var/lib/apt/lists/*	/usr/lib/unifi/data/*

# Install the UniFi sources
RUN echo 'deb https://www.ui.com/downloads/unifi/debian stable ubiquiti' >>  /etc/apt/sources.list.d/100-ubnt-unifi.list

# Update OS and install UniFi v5
# Wipe out auto-generated data
RUN apt-get -y update -q && \
	apt-get -y full-upgrade && \
    apt-get -y install openjdk-8-jre unifi  && \
	apt-get -y autoremove && \
	apt-get -y autoclean && \
	rm -rf /var/lib/apt/lists/*	/usr/lib/unifi/data/*

RUN dpkg -s unifi | grep -i version | tee /unifi-version

EXPOSE 8443/tcp 8080/tcp 8843/tcp 8880/tcp 3478/udp 10001/udp

VOLUME /usr/lib/unifi/data

WORKDIR /usr/lib/unifi

ENTRYPOINT ["java", "-Xmx256M", "-jar", "/usr/lib/unifi/lib/ace.jar"]
CMD ["start"]

