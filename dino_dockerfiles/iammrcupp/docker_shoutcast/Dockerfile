FROM ubuntu:14.04
MAINTAINER Aaron Cupp <IamMrCupp - mrcupp@mrcupp.com>
LABEL vendor="Tech-Noid Systems" \
      net.tech-noid.version="0.1.2" \
      net.tech-noid.server="Shoutcast Master" \
      net.tech-noid.release-date="2016-10-31" \
      net.tech-noid.version.is-production="false"
      

RUN mkdir /opt/shoutcast && \
    mkdir /var/log/shoutcast

WORKDIR /opt/shoutcast

RUN apt-get update && \
    apt-get install -y wget && \
    wget http://download.nullsoft.com/shoutcast/tools/sc_serv2_linux_x64-latest.tar.gz && \
    tar -xzvf sc_serv2_linux_x64-latest.tar.gz

VOLUME ["/etc/shoutcast"]

COPY shoutcast.conf /etc/shoutcast/

EXPOSE 10128 10129

ENTRYPOINT ["/opt/shoutcast/sc_serv", "/etc/shoutcast/shoutcast.conf"]
