# Horton Works Ambari Gateway

FROM ubuntu:14.04.3
MAINTAINER Dave Houston dave.houston@aimia.com

#### Installation

RUN locale-gen en_GB.UTF-8

RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9733A7A07513CAD
RUN apt-get update
RUN apt-get install wget -y
RUN wget -nv http://public-repo-1.hortonworks.com/ambari/ubuntu14/2.x/updates/2.1.2.1/ambari.list -O /etc/apt/sources.list.d/ambari.list
RUN apt-get update
RUN apt-get install -y ambari-server # && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN /usr/sbin/ambari-server setup -s

COPY start_ambari.sh /bin/

RUN chmod +x /bin/start_ambari.sh

#### Network

EXPOSE 8080

#### Services

ENTRYPOINT /bin/start_ambari.sh
