FROM ubuntu:14.04
MAINTAINER Devin Babb <devin.babb@ubnt.com>

VOLUME ["/var/lib/unifi-voip", "/var/log/unifi-voip", "/var/run/unifi-voip", "/usr/lib/unifi-voip"]

RUN echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen" > \
    /etc/apt/sources.list.d/21mongodb.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10

RUN echo "deb http://www.ubnt.com/downloads/unifi-voip/stage/debian stable ubiquiti" > \
    /etc/apt/sources.list.d/100-ubnt.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv 52F815F3

RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d

RUN apt-get update && \
    apt-get install binutils jsvc mongodb-server unifi-voip openjdk-7-jre-headless -f -y&& \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 9080/tcp 9443/tcp

ENTRYPOINT ["/usr/bin/java", "-Xmx1024M", "-jar", "/usr/lib/unifi-voip/lib/ace.jar"]
CMD ["start"]
