FROM ubuntu:precise

# Add MongoDB key
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
# Add Ubiquity key
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv C0A52C50

# Update sources
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise-security main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise-updates main restricted universe multiverse" >> /etc/apt/sources.list

RUN echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen" >> /etc/apt/sources.list.d/mongodb.list
RUN echo "deb http://www.ubnt.com/downloads/unifi/distros/deb/ubuntu ubuntu ubiquiti" > /etc/apt/sources.list.d/ubiquiti.list

# Install
RUN apt-get update && apt-get install -y unifi-beta

# Wipe out auto-generated data
RUN rm -rf /var/lib/unifi/*

EXPOSE 8080 8081 8443 8843 8880

VOLUME ["/var/lib/unifi"]
WORKDIR /var/lib/unifi

CMD ["/usr/lib/jvm/java-6-openjdk-amd64/jre/bin/java", "-Xmx1024M", "-jar", "/usr/lib/unifi/lib/ace.jar", "start"]
