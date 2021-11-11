#Minecraft PE Server
FROM centos:latest
MAINTAINER  Dr. Doom <doom@dev-ops.de>

#Setup enviroment variables
ENV CNAME="pocketmine"

#Update container
RUN yum update -y
RUN yum install -y vim sudo wget perl gcc g++ make automake libtool autoconf m4 gcc-multilib
RUN yum clean all

#Stage Files
COPY server.properties /tmp/server.properties
COPY start.sh /start.sh
RUN chmod 755 /start.sh

#Setup User
RUN useradd -d /data -s /bin/false --uid 1000 minecraft

#Setup container
EXPOSE 19132
VOLUME ["/data"]

#Start Pocketmine
WORKDIR /data
CMD ["/start.sh"]
