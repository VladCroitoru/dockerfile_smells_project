FROM ubuntu:14.04

MAINTAINER PsyKzz <matt.daemon660@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV SERVER_DIRECTORY=/opt/server
ENV OVERWRITE_DIRECTORY=/opt/server-overwrite

# Install dependencies
RUN apt-get update &&\
    apt-get install -y curl lib32gcc1

# Download and extract SteamCMD
RUN mkdir -p /opt/steamcmd &&\
    cd /opt/steamcmd &&\
    curl -s https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz | tar -vxz

# Create server dir
RUN mkdir -p ${SERVER_DIRECTORY}
ADD start.sh /opt/start.sh
RUN chmod 755 /opt/start.sh

# Create volume for server config
VOLUME /root/.avorion/galaxies/avorion_galaxy


# Ports required
EXPOSE 27000
EXPOSE 27000/udp
EXPOSE 27003
EXPOSE 27003/udp
EXPOSE 27020
EXPOSE 27021

# Admin steamID
ENV USER=nobody

CMD ["/opt/start.sh"]
