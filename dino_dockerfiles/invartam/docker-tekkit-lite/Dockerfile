FROM ubuntu:latest

RUN apt-get -y update && apt-get -y dist-upgrade \
    && apt-get -y install wget unzip default-jre

RUN mkdir /minecraft \
    && mkdir /data \
    && wget -O /data/server.zip http://servers.technicpack.net/Technic/servers/tekkitlite/Tekkit_Lite_Server_0.6.5.zip

ADD start.sh /data/start.sh
RUN chmod +x /data/start.sh

VOLUME /minecraft
EXPOSE 25565

WORKDIR /minecraft
ENTRYPOINT ["/data/start.sh"]
