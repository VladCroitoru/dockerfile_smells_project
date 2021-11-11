# Pull base image. (match this to elasticsearch)
FROM java:7
MAINTAINER Seán C McCord <ulexus@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y

# Common Deps
RUN apt-get -y install curl software-properties-common

# UniFi 4.x
RUN apt-get -y install binutils mongodb-server jsvc
RUN curl -L -o unifi_sysvinit_all.deb http://dl.ubnt.com/unifi/4.7.6/unifi_sysvinit_all.deb
RUN dpkg --install unifi_sysvinit_all.deb

# Wipe out auto-generated data
RUN rm -rf /var/lib/unifi/*

EXPOSE 8080 8081 8443 8843 8880

VOLUME ["/var/lib/unifi"]

WORKDIR /var/lib/unifi

CMD ["/usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java", "-Xmx1024M", "-jar", "/usr/lib/unifi/lib/ace.jar", "start"]
