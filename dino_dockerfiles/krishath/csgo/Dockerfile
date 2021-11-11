FROM phusion/baseimage:0.9.18
MAINTAINER Giulio De Pasquale <me@krishath.it>

ADD . /docker
CMD ["/sbin/my_init"]

# APPS INSTALL && CONFIG
RUN apt-get update && apt-get install -y lib32gcc1 wget
RUN chmod +x /docker/install_steamcmd.sh && useradd -m steam
RUN mkdir -p /home/steam/csgo/csgo/cfg 
RUN chown steam:steam /home/steam -R

VOLUME /home/steam/csgo/csgo/cfg

USER steam
CMD /docker/install_steamcmd.sh
EXPOSE 27015
EXPOSE 27015/udp
