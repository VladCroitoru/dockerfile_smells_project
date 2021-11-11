FROM ubuntu:latest

RUN apt-get -y update && apt-get -y dist-upgrade \
    && apt-get -y install wget unzip default-jre

RUN mkdir /minecraft \
    && mkdir /data \
    && wget -O /data/server.zip http://servers.technicpack.net/Technic/servers/tekkitmain/Tekkit_Server_v1.2.9g.zip

ADD start.sh /data/start.sh
RUN chmod +x /data/start.sh

VOLUME /minecraft
EXPOSE 25565

WORKDIR /minecraft
ENTRYPOINT ["/data/start.sh"]
