FROM ubuntu:16.04
MAINTAINER BILL WATTS <bill@billwatts.codes>

RUN echo "deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen" > \
  /etc/apt/sources.list.d/21mongodb.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10

RUN apt-get update && apt-get -y install wget binutils jsvc mongodb-10gen=2.4.14 openjdk-8-jre-headless

ARG DOCKER_UNIFI_VERSION=5.2.9
ENV DOCKER_UNIFI_VERSION ${DOCKER_UNIFI_VERSION}

RUN wget "http://dl.ubnt.com/unifi/${DOCKER_UNIFI_VERSION}/unifi_sysvinit_all.deb" \
    && dpkg -i unifi_sysvinit_all.deb \
    && rm -f unifi_sysvinit_all.deb

EXPOSE 8080/tcp 8081/tcp 8443/tcp 8880/tcp 3478/udp

ENTRYPOINT ["/usr/bin/java", "-Xmx1024M", "-jar", "/usr/lib/unifi/lib/ace.jar"]
CMD ["start"]
