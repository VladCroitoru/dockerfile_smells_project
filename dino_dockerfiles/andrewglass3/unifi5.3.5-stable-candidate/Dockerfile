FROM ubuntu:xenial
MAINTAINER Andrew Glass <andrew.glass@outlook.com>

VOLUME ["/var/lib/unifi", "/var/log/unifi", "/var/run/unifi", "/tmp/debs"]

RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" \
       > /etc/apt/sources.list.d/mongodb-org-3.0.list && \
       apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
       apt-get -qq update && \
       apt-get install -y wget mongodb-org openjdk-8-jre-headless binutils jsvc && \
       apt-get -f install && \
       mkdir -p /tmp/debs && \
       cd /tmp/debs && \
       wget https://www.ubnt.com/downloads/unifi/5.3.5-b92498c6/unifi_sysvinit_all.deb && \
       dpkg -i unifi_sysvinit_all.deb && \
       apt-get -f install 

EXPOSE 8080/tcp 8081/tcp 8443/tcp 8843/tcp 8880/tcp 3478/udp

WORKDIR /var/lib/unifi

ENTRYPOINT ["/usr/bin/java", "-Xmx1024M", "-jar", "/usr/lib/unifi/lib/ace.jar"]
CMD ["start"]
